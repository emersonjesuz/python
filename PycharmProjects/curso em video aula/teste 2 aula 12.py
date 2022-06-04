nome = str(input('qual o seu nome:'))
if nome == 'gustavo':                  # condições simples
    print('que nome lindo !')
print('tenha um bom dia {} '.format(nome))


nome1 = str(input('digite seu nome: '))
if nome1 == 'andre':
    print('ola que nom lindo :')        # condição composta
else:
    print('que nome mas o menos !')
print('tenha um bom dia {} '.format(nome1))


nome2 = str(input('\033[31mdigite seu nome\033[m :'))
if nome2 == 'gustavo ':
    print('que nome lindo !')
elif nome2 == 'pedro ' or nome2 == ' maria ' or nome2 == 'pedro':
    print('\033[33mseu nome é muito popular aqui no Brasil\033[m')   # condição aninhada
else:
    print('que nome comum')
print('tenha um bom dia {}'.format(nome2))