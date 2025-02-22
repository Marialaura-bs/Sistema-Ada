from config import db

class Trabalho(db.Model):
    __tablename__ = "trabalhos"

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    imagem = db.Column(db.String(300), nullable=False)  # Caminho da imagem
    link = db.Column(db.String(300), nullable=True)  # Opcional

    def __init__(self, titulo, descricao, imagem, link=None):
        self.titulo = titulo
        self.descricao = descricao
        self.imagem = imagem
        self.link = link

    def __repr__(self):
        return f'<Trabalho {self.titulo}>'
