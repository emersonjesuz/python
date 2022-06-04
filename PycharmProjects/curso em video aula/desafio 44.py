v1 = float(input('qual o peço do produto ?'))
print('''escolha uma forma de pagamento:\n
[1] Avista no dinheiro/chegue:
[2] Avista no cartão :
[3] Em ate 2x no cartao:
[4] 3x no cartão ou mais :\n''')
v2 = float(input('dogite uma opção:'))
if v2 == 1:
    avista = v1-(v1*10/100)
    print('\033[34mPARABENS!\033[m[1] acabou de adquiri um\n\033[34mBONUS\033[m de 10% de desconto ao escolher essa forma pra pagar seu produto! ')
    print('o preço é :\033[33 R${:.2f}\033[m \n+ o BONUS no valor vai fica:\033[33m R${:.2f}'.format(v1,avista))


elif v2 == 2:
    cartaoV = v1-(v1*5/100)
    print('\033[34mPARABENS![2]\033[m : \033[34mBONUS\033[m\ncom o BONUS você acabou de ganhar 5% de desconto, nessa forma de pagamento!')
    print('o valor : \033[33R${:.2f} \033[m\n+ o BONUS no valor vai ficar :\033[33m R${:.2f} '.format(v1,cartaoV))
elif v2 == 3:
    cartao2 = v1 / 2
    print('opção :[3]\n \033[33m2x de R${:.2f} sem juros'.format(cartao2))
elif v2 == 4:
    c3 = (v1 + (v1 * 20 / 100)) / 3
    c4 = (v1 + (v1 * 20 / 100)) / 4
    c5 = (v1 + (v1 * 20 / 100)) / 5
    c6 = (v1 + (v1 * 20 / 100)) / 6
    print('''produto:R${:.2f}
        \033[33m3x de R${:.2f} 20% de juros
        4x de R${:.2f} 20% de juros
        5x de R${:.2f} 20% de juros
        6x de R%{:.2f} 20% de juros\033[33m'''.format(v1, c3, c4, c5, c6))
else:
    print('\033[31mopção invalida !\033[m \ntente novamente')

