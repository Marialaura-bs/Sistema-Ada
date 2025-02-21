from config import db
from flask_login import UserMixin

class Mensagens(db.Model, UserMixin):
    __tablename__ = "mensagens"
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    mensagem = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_mensagens_user_id'), nullable=True)  # Definir um nome para a restrição de chave estrangeira
    user = db.relationship('User', backref=db.backref('mensagens', lazy=True))

    def __init__(self, mensagem=None, user_id=None):
        self.mensagem = mensagem
        self.user_id = user_id
    
    def __repr__(self):
        return f'<Mensagens {self.mensagem}>'