from exer115.lib.interface import *
from exer115.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = Menu(['lista de pessoas ', 'cadastra novas pessoas', 'sair do sistema'])
    if resposta == 1:
        #função de listagem de pessoas e ler um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho(roxo('cadastro de pessoas'))
        nome = str(input('Nome:'))
        idade = leiaInt('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('saindo do programa . . . ')
        break
    else:
        print('\033[31m ERRO""" USE APENAS AS OPÇÕES ACIMA!\033[m')
    sleep(2)
