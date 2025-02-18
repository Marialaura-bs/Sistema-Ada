from flask import Blueprint, request, render_template, flash, redirect, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.usuario import User
from flask_login import login_user, logout_user, login_required
from config import db  # Aqui estamos importando o db

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@user_bp.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        data = request.form

        if User.query.filter_by(email=data['email']).first():
            return redirect(url_for('user.login'))  # Alterado aqui

        hashed_password = generate_password_hash(data['senha_login'])
        is_admin = data.get('is_admin') == 'on'
        new_user = User(name=data['usuario_login'], email=data['email'], senha=hashed_password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('user.login'))  # Alterado aqui
    else: 
        return redirect(url_for('user.cadastro'))  # Alterado aqui, se necessário

@user_bp.route('/conectar', methods=['GET', 'POST'])
def conectar():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(email=data['email']).first()
        
        if user and check_password_hash(user.senha, data['senha']):
            login_user(user, remember=True)
            return redirect(url_for('user.rede_apoio'))  # Sem alteração aqui
        else:
            flash('Email ou senha incorretos', 'danger')
            return redirect(url_for('user.login'))  # Alterado aqui

    return render_template('login.html')

@user_bp.route('/logoff')
def logoff():
	logout_user()
	return redirect('/')

@user_bp.route('/rede_apoio')
@login_required
def rede_apoio():
    return render_template('rede_de_apoio.html') 
