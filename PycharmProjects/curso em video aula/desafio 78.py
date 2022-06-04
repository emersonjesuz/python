num = list()
maior = menor = 0
for cont in range(0, 5):
    num.append(int(input('digite um valor na posição {}: '.format(cont))))
    maior = max(num)
    menor = min(num)
print('-='*20)
print(f'os numeros escolhidos são {num}')
print(f'o maior numero é {maior} e esta na posição ', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print(f'o menor numero é {menor} e esta na posição ', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()
