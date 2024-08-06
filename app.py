from flask import Flask, render_template, request

app = Flask(__name__)

@app.route ('/')
def index():
    return render_template('index.html')

@app.route ('/conheca')
def conheca():
    return render_template('conheca.html')

@app.route ('/nossos_trabalhos')
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

@app.route('/rede_de_apoio', methods=['post'])
def rede_de_apoio():
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    if usuario== "alba.lopes" and senha=="12345":
        return render_template('rede_de_apoio.html', usuario=usuario)
    else:
        return "Usuário ou senha incorretos"
    
@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")