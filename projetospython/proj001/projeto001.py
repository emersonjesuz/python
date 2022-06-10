
from distutils.log import debug
from flask import Flask, request, render_template
from connect import mostrarTodos,atualizarPessoa,deletarPessoa,inserir
from model import pessoa



app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index(): 
    return render_template('index.html')

@app.route('/')
def usuario():
    cpf = request.form['cpf']
    nome = request.form['pessoa']
    dataNascimento = request.form['data']
    pessoa = (cpf,nome,dataNascimento)
    inserir(pessoa)



if __name__=='__main__':
    app.run(debug=True)