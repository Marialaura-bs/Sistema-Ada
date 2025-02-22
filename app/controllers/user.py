from flask import Blueprint, request, render_template, flash, redirect, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.usuario import User
from app.models.mensagens import Mensagens
from app.models.conteudo import Trabalho
from flask_login import login_user, logout_user, login_required, current_user
from config import db  # Aqui estamos importando o db
from sqlalchemy.orm import joinedload
import os
from werkzeug.utils import secure_filename

user_bp = Blueprint('user', __name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@user_bp.route('/upload', methods=['POST'])
def upload_trabalho():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    link = request.form.get('link')  # Pode ser None

    # Verifica se o arquivo foi enviado
    if 'file' not in request.files:
        return "Nenhuma imagem enviada", 400

    file = request.files['file']

    if file.filename == '':
        return "Nenhuma imagem selecionada", 400

    # Garante que a pasta de upload existe
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Garante um nome seguro para o arquivo (remove espaços e caracteres inseguros)
    filename = secure_filename(file.filename).replace(" ", "_")

    # Caminho completo para salvar a imagem
    caminho_imagem = os.path.join(UPLOAD_FOLDER, filename)
    file.save(caminho_imagem)

    # Salva apenas o caminho relativo ao `static/`
    caminho_imagem_relativo = os.path.join('uploads', filename)  # 'uploads/nome_do_arquivo.jpg'

    # Salva os dados no banco de dados
    novo_trabalho = Trabalho(
        titulo=titulo,
        descricao=descricao,
        imagem=caminho_imagem_relativo,  # Apenas o caminho relativo
        link=link
    )

    db.session.add(novo_trabalho)
    db.session.commit()

    return redirect(url_for('user.nossos_trabalhos'))

@user_bp.route('/nossos_trabalhos')
def nossos_trabalhos():
    trabalhos = Trabalho.query.all() 
    return render_template('nossos_trabalhos.html', trabalhos=trabalhos)
  
@user_bp.route('/user')
def usuarios():
    usuarios = User.query.all()  # Alterado de 'user' para 'User'
    return jsonify([usuario.as_dict() for usuario in usuarios])

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@user_bp.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        data = request.form

        if User.query.filter_by(email=data['email']).first():
            return redirect(url_for('user.login'))

        hashed_password = generate_password_hash(data['senha_login'])
        is_admin = data.get('is_admin') == 'on'
        new_user = User(name=data['usuario_login'], email=data['email'], senha=hashed_password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('user.login'))  
    else: 
        return redirect(url_for('user.cadastro'))  

@user_bp.route('/conectar', methods=['GET', 'POST'])
def conectar():
    if request.method == 'POST':
        
        user = User.query.filter_by(email=request.form['email']).first()
        
        if user and check_password_hash(user.senha, request.form['senha']):
            login_user(user, remember=True)
            return render_template('rede_de_apoio.html')   
        else:
            flash('Email ou senha incorretos', 'danger')
            return redirect(url_for('user.login')) 


@user_bp.route('/logoff')
def logoff():
	logout_user()
	return redirect('/')


@user_bp.route('/rede_apoio')
@login_required
def rede_apoio():
    mensagens = Mensagens.query.options(joinedload(Mensagens.user)).all()
    return render_template('rede_de_apoio.html', mensagens=mensagens)


@user_bp.route('/mensagens', methods=['POST'])
def mensagens():
    if request.method == 'POST':
        data = request.form
        nova_mensagem = Mensagens(mensagem=data['mensagens'], user_id=current_user.id)  # Associa a mensagem ao usuário logado
        db.session.add(nova_mensagem)
        db.session.commit()
    return redirect(url_for('user.rede_apoio'))
    