cont = valor = c = resul = 0
while True:
    valor = int(input('deseja ver a tabuada de qual valor ? '))
    print('-'*30)
    cont += 1
    if valor <= 0:
        break
    for c in range(1, 11):
        resul = valor * c
        print(f'{valor}x{c}={resul}')
    print('-'*30)
print('programa finalizado. . .')
