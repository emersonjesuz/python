matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = mai = col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite o valor para [{l}, {c}] :'))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('=-'*30)
print(f'a soma de todos os numeros pares é {pares}')
for l in range(0, 3):
    col += matriz[l][2]
print(f'a soma da terceira coluna é {col}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f'o maior nuero da coluna dois é {mai}')
