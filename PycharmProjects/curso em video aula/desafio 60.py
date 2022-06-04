n = int(input('digite um numero pra calcular seu fatorial :'))
c = n
f = 1   # se for mutiplicar f = 1 porque se for zero ovalor sempre vai ser zero
#print('calculando o {}! = '.format(n), end='')
#while c > 0:
   # print('{}'.format(c), end='')
  #  print(' x 'if c > 1 else '= ', end='')
 #   f *= c
#    c -= 1
#print('{}\n'.format(f))
print('calculando o {}! = '.format(n), end='')
for h in range(n-1, 0, -1):
    print('{}'.format(c), end='')
    print(' x 'if h > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))