valor = list()
for cont in range(0, 5):
    n = int(input('digite um valor '))
    if cont == 0 or n > valor[-1]:
        valor.append(n)
        print('foi  adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                print(f'vai ser adicionado na {pos} da lista')
                break
            pos += 1
print('=-'*30)
print(f'os valores adicionados a lista {valor}')
