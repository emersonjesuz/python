from random import randint
from time import sleep
jogo = []
lista = []
print('-'*40)
print('{:^40}'.format('JOGO DA MEGA SENA '))
print('-'*40)
contnu = 1
quant = int(input('quantos jogos você quer que eu sorteie ? '))
while contnu <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    contnu += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-='*3)
sleep(1)
for i, l in enumerate(jogo):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '=-' * 5)
