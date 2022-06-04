
from random import randint
cont = numero = menor = maior = c = 0  # a forma de fazer o computador montar uma tupla aleatoria usando randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'os valores sorteados são :', end=' ')
for c in numero:
    cont += 1
    print(f'{c}', end=' ')
   # if cont == 1:
      #  menor = maior = c
   # else:
    #    if c < menor:    forma normal de saber qual o maior e o menor
     #       menor = c
      #  if c > maior:
      #      maior = c
print(f'\no menor numero {max(numero)}')  # uma tupla nos permite usar "max" para o maior "min" para o menor valor na tupla
print(f'o maior numero {min(numero)}')
