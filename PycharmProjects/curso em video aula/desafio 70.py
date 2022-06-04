f = produto = opçao = barato = ''
preço = soma = cont = menor = cont1000 = 0
print('=='*20)
print(f'{f:^10}MERCADINHO BOM PREÇO ')
print('=='*20)

while True:
    produto = str(input('qual o produto ?'))
    preço = float(input('preço: R$'))
    soma += preço
    cont += 1
    if cont ==1 or preço < menor:
        menor = preço
        barato = produto
    if preço >= 1000:
        cont1000 += 1

    opçao = ' '
    while opçao not in 'NS':
        opçao = str(input('deseja continuar ? [S / N]')).strip().upper()[0]
    if opçao == 'N':
        break
print(f'o total dos valores é R${soma:.2f}\ntem {cont1000} produtos custa mais  que R$1000.00')
print(f'o produto mas barato é {barato} ele custa R${menor:.2f}')
