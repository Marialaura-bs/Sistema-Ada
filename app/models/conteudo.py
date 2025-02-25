from config import db

class Trabalho(db.Model):
    __tablename__ = "trabalhos"

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(300), nullable=True)  # Opcional

    def __init__(self, titulo, descricao, link=None):
        self.titulo = titulo
        self.descricao = descricao
        self.link = link

    def __repr__(self):
        return f'<Trabalho {self.titulo}>'
