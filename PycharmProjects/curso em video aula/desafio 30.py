#numero =int(input('digite um numeron:'))
#lista=[0,1,2,3,4,...]
#if lista[::1]==numero>=0:
#    print('par')
#else:
  #  print(('impar'))
numero=int(input('digite um numero :'))     # exercicio pra saber se o numero e impar ou par
m = numero%2
if m == 1:
    print('o numero {} é IMPART'.format(numero))
else:
    print('o numero {} é PAR {}'.format(numero, m))
