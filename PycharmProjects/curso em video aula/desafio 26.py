frase=(str(input("digite uma frase :"))).strip().upper()
print('essa frsse tem "{}" letras A'.format(frase.count('A')))
print('a primeira  letra "A" começa no {}  '.format(frase.find("A")))
print('e a ultima  letra "A" termina no {}'.format( frase.rfind('A')))