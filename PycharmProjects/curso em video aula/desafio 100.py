from random import randint
from time import sleep


def somapar():
    lista = []
    soma = total = cont = 0
    while True:
        cont += 1
        total = randint(1, 10)
        lista.append(total)
        if total % 2 == 0:
            soma += total
        if cont == 5:
            break
    print(f'Sorteando {len(lista)} da lista: ', end=' ')
    for v in lista:
        print(v, end=' ')
        sleep(0.5)
    print('PRONTO!')
    sleep(0.5)
    print(f'Somando os valores pares de  {lista}, Temos {soma} ')


print('~' * 50)
somapar()
print('~' * 50)
