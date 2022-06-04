lista = list()
lisimpar = list()
lispar = list()
while True:
    lista.append(int(input('digite um numero')))
    lista.sort()
    opc = ' '
    while opc not in 'SN':
        opc = str(input('deseja continua? [S/N]')).strip().upper()[0]
    if opc == 'N':
        break
for c, v in enumerate(lista):
    if v % 2 == 1:
        lisimpar.append(v)
    if v % 2 == 0:
        lispar.append(v)
print(f'os numeros digitados {lista}')
print(f'os numeros impar {lisimpar}')
print(f'os numeros pares {lispar}')
