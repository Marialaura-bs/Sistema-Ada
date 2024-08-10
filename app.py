from flask import Flask, render_template, request
from flask import flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'

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
        flash("Login ou senha incorretos")
        return redirect("/login")
    
    
@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

lista_mensagens = []
@app.route('/mensagens', methods=['post', 'get'])
def mensagens():
    mensagens = request.form['mensagens']
    lista_mensagens.append(mensagens)
    return render_template('rede_de_apoio.html', mensagens=mensagens, lista=lista_mensagens)