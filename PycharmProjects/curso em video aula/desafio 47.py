for numero in range(2,51,2): # ocupa menos processador repete 2 laços
    print('{}'.format(numero),end=' ')
print('acabou')

for numero in range(1,51):      # ocupa mas do processador  repete 3 laços
    if numero % 2 == 0:
        print(numero,end=' ')
print('acabou')