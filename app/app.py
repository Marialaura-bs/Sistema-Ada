from flask import Flask, render_template, request, flash, redirect
from config import db
from config import lm
from flask_migrate import Migrate
from app.models.usuario import User
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.controllers.user import user_bp
from app.controllers.home import home_bp
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'ada')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    lm.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(home_bp)

    @lm.user_loader
    def load_user(id):
        return User.query.get(id)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/conheca')
    def conheca():
        return render_template('conheca.html')

    @app.route('/nossos_trabalhos')
    def nossos_trabalhos():
        return render_template('nossos_trabalhos.html')

    @app.route('/lovelace')
    def lovelace():
        return render_template('lovelace.html')

    @app.route('/dados')
    def dados():
        return render_template('dados.html')

    @app.route('/login', methods=['post', "get"])
    def login():
        return render_template('login.html')
        
    
    @app.route('/cadastro')
    def cadastro():
        return render_template("cadastro.html")
    
    lista_mensagens = []
    @app.route('/mensagens', methods=['post', 'get'])
    def mensagens():
        mensagens = request.form['mensagens']
        lista_mensagens.append(mensagens)
        return render_template('rede_de_apoio.html', mensagens=mensagens, lista=lista_mensagens)

    with app.app_context():
        db.create_all()

    return app