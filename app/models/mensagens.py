from config import db
from flask_login import UserMixin
   
class Mensagens(db.Model, UserMixin):
   __tablename__ = "mensagens"  # nome da tabela no banco de dados

    # Definindo a coluna ID como chave primária
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    mensagem = db.Column(db.String(500), nullable=False)
    
    # Construtor para inicializar a mensagem
    def __init__(self, mensagem=None):
        self.mensagem = mensagem
    
    # Representação da classe
    def __repr__(self):
        return f'<Mensagens {self.mensagem}>'
