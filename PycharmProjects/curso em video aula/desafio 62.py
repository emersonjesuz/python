print('GERADOR DE PA')
print('-='*10)
primeiro = int(input('primeiro termo :'))
razão = int(input('qual a razão ?'))
termo = primeiro
cont = 1
total = 0
mais =10
while mais != 0:
    total = total + mais
    while cont <= total:
        termo += razão
        cont += 1
        print('{} -=- '.format(termo), end='')
    print('PAUSE')
    mais = int(input('quantos termos você quer mostra a mas ?'))
print('progressão finalizada com {} termos mostrado'.format(total))
