from config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
   __tablename__="users"
   id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
   name = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String(100), nullable=False, unique=True, name='email')
   senha = db.Column(db.String(100), nullable=False)
   is_admin = db.Column(db.Boolean, default=False)
   
   def __init__(self, name, email, senha, is_admin=False):
    self.name = name
    self.email = email
    self.senha = senha
    self.is_admin = is_admin
   def __repr__(self):
     return f'<User {self.name}>'
   
   def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'is_admin': self.is_admin
        }
