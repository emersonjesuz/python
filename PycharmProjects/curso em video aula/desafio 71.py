
print('=='*20)
print('{:^30}'.format('BANCO FULLMO'))
print('=='*20)
valor = int(input('qual valor gostaria de sacar R$ '))
total = valor
ced = 200
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0: # assim so mostra  as cedulas que tem contador maior que 0
            print(f'total de {contced} cedulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        contced = 0
        if total == 0:
            break
print('='*40)
print('volte sempre ao BANCO FULLMO!')
