from exer115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # 'rt' vai verificar se existe o arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # 'wt+' vai verificar se existe se não existir  criar um arquivo
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
       a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        #print(a.read())
        #cabecalho('pessoas cadastradas')
        for lista in a:
            print(lista)
            #print(f'{lista[0:-8]:<30}{lista[-8:]:>3}')
            #lista.replace('\n', '')
    #finally:
     #   a.close()                   #readline vai ler apenas a primeira linha


def cadastrar(arqui, nome='desconhecido', idade=0,sexo = 'desconhecido', cpf=000, rg=0):
    try:
        a = open(arqui, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{"nome"}: {nome}, {idade} - {"Anos"}, {"sexo"} = {sexo} , {"CPF"} : {cpf} , {"RG"} : {rg}\n')
            print(end='')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
