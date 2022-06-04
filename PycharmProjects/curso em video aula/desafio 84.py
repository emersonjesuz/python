temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('nome:')))
    temp.append(float(input('peso:')))
    opc = str(input('deseja continua ? [S/N] :')).strip().upper()[0]
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]      # forma de fazer  maior ou menor entre listas
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()     # usando o clear ele vai limpar a primeira lista assim que salva os dados na segunda lista
    if opc == 'N':   # assim não faz com que sempre a segunda copie tudo da primeira e va repetindo infinitamente
        break
print('=-'*30)
print(f'foram {len(princ)} pessoas cadastradas ')
print(f'o maior peso é {mai}Kg. e foi de ', end=' ')
for p in princ:
    if p[1] == mai:    # assim você faz pra aparecer o nome da pessoa na msm linha do peso
        print(f'[{p[0]}] ', end=' ')  # usando o p[0] ele vai pega sempre a primeira informaçao que é igual a maior ou a menor
print()
print(f'o menor peso foi {men}Kg, e foi de ', end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]  ', end=' ')
print()
