from config import db
from flask_login import UserMixin
from app.models.usuario import User
   
class Mensagens(db.Model, UserMixin):
    __tablename__ = "mensagens"  # nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    mensagem = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Relacionamento com User
    user = db.relationship('User', backref=db.backref('mensagens', lazy=True))  # Definindo o relacionamento com a tabela User

    # Construtor para inicializar a mensagem
    def __init__(self, mensagem=None, user_id=None):
        self.mensagem = mensagem
        self.user_id = user_id
    
    # Representação da classe
    def __repr__(self):
        return f'<Mensagens {self.mensagem}>'
