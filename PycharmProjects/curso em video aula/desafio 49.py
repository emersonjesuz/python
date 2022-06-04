print('-=-'*20)
print('{:^45}'.format('TABUADA')) # exercicio 9  so que usando laços
print('-=-'*20)
tabuada = int(input('{:^10}qual numero você quer saber ?'.format(' ')))
for c in range(1,11):
    print('{:^20}{}x{}={}'.format('',tabuada, c,tabuada*c))