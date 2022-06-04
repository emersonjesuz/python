list = []
while True:
    n = int(input('digite um valor'))
    list.append(n)
    op = ' '
    while op not in 'NS':
        op = str(input('deseja continuar? [S/N] :')).strip().upper()[0]
    if op == 'N':
        break
print('=-'*30)
list.sort(reverse=True)
print(f'foram {len(list)} numeros digitados')
print(f'os numeros são {list}')
print('o valor 5 ', end=' ')
if 5 in list:
    print(f'sim, foi encotrado na lista esta na  posição {list.index(5)}', end='')
else:
    print('nao foi encontrado !', end=' ')
