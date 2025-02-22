from flask import Flask, render_template, request, redirect, url_for
from config import db
from config import lm
from flask_migrate import Migrate
from app.models.usuario import User
from flask_login import login_required, current_user
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
    lm.login_view = 'user.login'
    lm.login_message = "Por favor, faça login para acessar esta página."
    lm.login_message_category = "info"
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

    @app.route('/lovelace')
    def lovelace():
        return render_template('lovelace.html')

    @app.route('/dados')
    def dados():
        return render_template('dados.html')
    
    @app.route('/form_adm')
    def form_adm():
        return render_template('formulario_adm.html')
        
    @app.route('/cadastro')
    def cadastro():
        return render_template("cadastro.html")

    with app.app_context():
        db.create_all()

    return app