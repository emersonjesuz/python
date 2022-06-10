
from tinydb import TinyDB,Query
from model  import pessoa

bd = TinyDB('projetospython/proj001/Pessoas.json')
usuario = Query()
def inserir(model: pessoa):
    bd.insert({'CPF':model.CPF,'nome':model.nome,'dataNascimento':model.dataNascimento})

def mostrarTodos():
    todos = bd.all()
    for t in todos:
        print(t)
    
    

def deletarPessoa(cpf:int):
    if bd.search(usuario.CPF==cpf):
        bd.remove(usuario.CPF==cpf)
        print('Usuario Deletado com sucesso')
    else:
        print('Usuario não encontrado')

def atualizarPessoa(cpf:int, model:pessoa):
    if bd.search(usuario.CPF==cpf):
        bd.remove(usuario.CPF==cpf)
        inserir(model)
    else:
        print(f'Usuario Não encontrado tente novamente')