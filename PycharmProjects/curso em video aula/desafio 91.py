from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jogador1': randint(1, 6),
            'jogador2': randint(1, 6),
            'jogador3': randint(1, 6),
            'jogador4': randint(1, 6)}
li = []
for ti, co in jogadas.items():
    print(f'   o {ti}  tirou  {co}')
    sleep(1.5)
print(' = = Ranking dos jogadores = = ')
li = sorted(jogadas.items(), key=itemgetter(1), reverse=True) # forma de colocar um dicionario em ordem
for i, v in enumerate(li):  # voce tem que colocar dentro de uma lista e olocar o sort
    print(f'      {i+1}° {v[0]} com {v[1]}')
    sleep(1)
