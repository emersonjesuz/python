
n1 = int(input('digite um número: '))
n2 = int(input('digite outro número:'))
n3 = int(input('digite mais um número: '))
n4 = int(input('digite o ultimo número: '))
tupla = (n1, n2, n3, n4)
print(f'você digitou os valores {tupla}')
print(f'o 9 aparece {tupla.count(9)} vez')
if 3 in tupla:
    print('o valor 3 aparece na {}° posição'.format(tupla.index(3)+1))
else:
    print('o valor 3 aparece em nenhuma posição')
print('os numero pares são ', end=' ')
for c in tupla :
    if c % 2 == 0:
        print(c,end=' ')

