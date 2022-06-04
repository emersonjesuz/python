num = list()
while True:
    n = int(input('digite um valor :'))
    if n not in num:
        num.append(n)
        print('adicionado com susesso !')
    else:
        print('valor duplicado! não vou adicionar! ')
    opc = str(input('deseja continuar [S/N] :')).strip().upper()[0]
    if opc in 'N':
        break
num.sort()
print('=-'*30)
print(f'você adicionou os valores {num}')