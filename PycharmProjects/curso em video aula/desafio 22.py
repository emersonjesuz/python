nome=str(input('qual o seu nome completo?')).strip()
print('seu nome em miúsculo é: ',nome.upper())
print('seu nome em minuculo é:',nome.lower())
print(len(nome.strip()))

print('ANALISANDO SEU NOME ...')
print('seu nome em maiuscúla é {}'.format(nome.upper()))
print('seu nome em minusculo é {}'.format(nome.lower()))
print('seu nome ao todo tem {}'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letra'.format(nome.find(' '))) # duas formas de fazer
separa=nome.split()
print('seu primeiro nome é {} e ele tem {} letras '.format(separa[0],len(separa[0])))
