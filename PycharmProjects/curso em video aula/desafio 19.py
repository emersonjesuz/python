import random
paula=input('digite um nome um por um:')
ada=input('digite o segundo nome:')
elem=input('digiteo terceiro nome:')
marcos=input('digite o qurto nome')
lista = [paula,ada,marcos,elem]
n1=random.choice(lista)
print('o nome do aluno que vai apagar o quadro é {}'.format(n1))