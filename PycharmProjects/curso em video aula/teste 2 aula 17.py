#valores = []
valores = list()  # da pra criar uma lista vazia dessas duas formas ai !
valores.append(5)
valores.append(3)  # append adciona itens a lista
valores.append(8)
#for v in valores:
 #   print(f'{v}...', end='')  # usando o for para deixa a lista mas bonita  e end= pra fazer ela ficar em seguencia
for cont in range(0, 5):
    valores.append(int(input('digite um valor ')))   # forma de fazer uma lista interativa aonde ele vai perguntar os valores
for c, v in enumerate(valores):
    print(f'na posição {c} encotrei o valor {v}!')# forma de enumera o valor e fazer um print com todos os itens e sua contidade
print('cheguei ao final')