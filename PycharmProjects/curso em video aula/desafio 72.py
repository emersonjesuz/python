tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trêze',
         'cartorze', 'quize', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
numero = cont = 0
opçao = ' '
print('0'*30)
print('{:^35}'.format('\033[31mnumeros por extenso\033[m'))
print('0'*30)
while True:
    numero = int(input('\ndigite um numero entre 0 e 20 : '))
    if 0 <= numero <= 20:  # assim ele vai da limite de o e vinte impedindo de colocar nem menor nem maior
        print(f'o numero escolhido é {tupla[numero]}')
        cont += 1
    else:
        print('tente novamente .', end=' ')
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('deseja prosseguir? [S/N]')).strip().upper()[0]
    if opçao == 'N':
        break
print('\033[33mfinalizando programa. . .')
print(f'você escolheu {cont} numero !')
