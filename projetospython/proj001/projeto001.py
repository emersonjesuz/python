from distutils.log import debug
from unicodedata import name
from unittest import result
from flask import Flask, flash, request, render_template
from connect import mostrarTodos,atualizarPessoa,deletarPessoa,inserir
from model import pessoa



app = Flask(__name__)
@app.route('/')
def index(): 
    nome = mostrarTodos()
    return render_template("index.html",nome = nome)

@app.route('/')
def usuario():
    nome = request.form['pessoa']


if __name__=='__main__':
    app.run(debug=True)