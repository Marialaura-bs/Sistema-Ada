from flask import Blueprint, request, render_template, flash, redirect, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.usuario import User
from flask_login import login_user
from config import db  # Aqui estamos importando o db

user_bp = Blueprint('user', __name__)

@user_bp.route('/user')
def usuarios():
    usuarios = User.query.all()  # Alterado de 'user' para 'User'
    return jsonify([usuario.as_dict() for usuario in usuarios])  # Supondo que você tenha um método as_dict() no seu modelo


@user_bp.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        data = request.form

        if User.query.filter_by(email=data['email']).first():  # Alterado de 'user' para 'User'
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(data['senha_login'])
        is_admin = data.get('is_admin') == 'on'
        new_user = User(name=data['usuario_login'], email=data['email'], senha=hashed_password, is_admin=is_admin)  # Alterado de 'user' para 'User'
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('user.usuarios'))
    else: 
        return redirect(url_for('cadastro'))

@user_bp.route('/conectar', methods=['GET', 'POST'])
def conectar():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.senha, data['senha']):
            login_user(user)
            return render_template('rede_de_apoio.html')  # Supondo que você tenha esse template
        else:
            flash('Email ou senha incorretos')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
