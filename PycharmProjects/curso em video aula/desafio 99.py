from time import sleep


def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados. . .')
    for valor in num:
        print(valor, end=' ')
        sleep(0.2)
        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont += 1
    print(f' foram informados {cont} valores ao todo.')
    print(f'O maior valor é {maior}')
    print('-=' * 20)


print('-=' * 20)
maior(2, 3, 6, 9, 1)
maior(4, 5, 8, 0)
maior(9)
maior()
