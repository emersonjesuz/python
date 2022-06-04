nome = input('digite seu nome ')
print('\033[31m -=-\033[m'*20)
print('ola {}, vamos nos conhecer melhor ?'. format(nome))
print('\033[31m -=-\033[m'*20)


cores = {'verde': '\033[32m',
         'amarelo':'\033[33m',  # abraa aspas dentro do cochete
         'azul':'\033[34m',
         'preto e branco':'\033[7;30m',
         'vermelho':'\033[31m',
         'neutra':'\033[m'}
print('{}ola{} {}{} bem vindo \033[m {} ao seu lar \033[m'.format(cores['amarelo'],cores['azul'],nome,cores['preto e branco'],cores['vermelho']))