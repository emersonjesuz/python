#import random
from random import shuffle
n1= input('mencione o primeiro nome:')
n2=input('mencione o segundo nome:')
n3=input('mencione o terceiro nome:')
n4=input('mencione o querto nome:')
lista=[n1,n2,n3,n4]
#random.shuffle(lista)
shuffle(lista)
#print('os aluno vão apresentar nessa seguencia {}'.format(lista))
print('a seguncia é')
print(lista)