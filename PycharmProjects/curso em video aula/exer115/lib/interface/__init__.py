from exer111.utilidadescev.dados import leiaInt
from exer115.lib.cores import *

def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    txt.upper()
    print(linha())
    print(txt.center(42))
    print(linha())


def Menu(lista):
    cabecalho('MENU PRICIPAL')
    cont = 1
    for itens in lista:
        print(f'{azul(cont)}-{amarelo(itens)}')
        cont += 1
    print(linha())
    opc = leiaInt('sua opção:')
    return opc
