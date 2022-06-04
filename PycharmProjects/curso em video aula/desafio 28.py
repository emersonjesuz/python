#import random
#print('estou pensando em um numero de  0 a 5 . . .')
#numero=int(input('qual seria esse numero?'))
#n1=random.randint(0,5)
#print('{}'.format(n1))

from random import randint
from time import  sleep    #  biblioteca time / serve pra tempo
computador=randint(0,5) # esse comando faz o computador 'pensar' aleatoriamente
print('-=-'*20)
print('vou pensa em um numero entre 0 e 5 tente adivinha ! ')
print('-=-'*20)
jogador= int(input('em que numero eu pensei ?')) # jogador tenta adivinhar
print('PROCESSANDO . . .')
sleep(3) # função da biblioteca time
if jogador == computador:
    print('PARABENS, você conseguiu me vencer !')
else:
    print('GANHEI! eu pensei no numero {} e você no numero {} !'.format(computador,jogador))