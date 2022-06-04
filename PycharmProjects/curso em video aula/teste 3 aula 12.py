nome = str(input('qual o seu nome ?'))
if nome == ' gustavo':
    print('seu nome é muito foda!')
elif nome in 'ana maria paula sandra jessica':
    print('seu nome é um nome comum e bem feminino !')
elif nome == 'pedro' or nome == 'antonio' or nome == 'pedro ':
    print('seu nome é bem comum !')
else:
    print('seu nome é normal !')
print('tenha um bom dia, {}'.format(nome))