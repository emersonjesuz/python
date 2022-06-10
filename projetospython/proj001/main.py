
from connect import inserir,mostrarTodos
from model import pessoa
from connect import deletarPessoa
from connect import atualizarPessoa


def main():
    pe = pessoa(1235359,"mathues", "00-08-1999")
    pe2 = pessoa(1111111,'marco','12-07-1998')
    t = mostrarTodos()
    

    print(f'{t["CPF"]}')
main()