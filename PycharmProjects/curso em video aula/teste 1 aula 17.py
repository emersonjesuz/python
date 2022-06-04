num = [2, 5, 9, 1]  # uma lista precisa de cochete
num[2] = 3   # forma de troca um item por outro na lista
num.append(7) # usando append pra adicionar mas um item na lista
num.sort()  # sort vai colocar tudo em ordem alfabetica ou numerica
num.sort(reverse=True)  # reverse vai colocar em ordem mas aucontrario
num.insert(2, 3)   # insert vai inserir o item na posição desejada exp: na posição 2 inserir o item 4
num.pop(0) # usando o pop pra remover itens da lista === mas se deixa o pop() em branco ele remove o ultimo item da lista
num.remove(2) #usando o remove ele vai remover o item pelo " nome do item " mas se tiver dois items iguais ele tira o primeiro
if 4 in num: # se o 4 in num ... assim ele vai evitar de da erro caso tente remover um item que nao existe na lista
    num.remove(4)
else:     # se ele  achar o numero 4 ele remove se nao ele mostra o print
    print('não achei o numero 4')
print(num)
print(f'essa lista tem {len(num)} itens') # len do num pra saber quantos itens tem na lista