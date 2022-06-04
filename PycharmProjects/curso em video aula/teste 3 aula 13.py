n = int(input('digite um numero :'))
for c in range (0,n+1):    #  ( n ) pode adicionar na range
    print(c)               # se colocar n+1 a range vai ate o numero de ( n )

i = int (input("digite  o inicio "))
f = int(input('digite o fim '))
p = int ( input(' digite o paso '))
for c in range(i,f+1,p):
    print(c)       # sempre o ( paso ) vai ser as contidade de vezes que vai pula entre o inicio e o fim

for c in range(0,3):
    n = int(input('digite um numero ')) # se o 'digite um valor ' for dentro de 'for' de acordo com a range
                                        # ele vai se repetir e falar 'digite um numero'

s = 0
for c in range(0,4):
    n = int (input('digite um valor'))
    s += n          #' s+= n' é assim que faz a abreviação da  soma s = s + n  sendoque ja tem o valor de s
print('a soma entre todos os valores : {}'.format(s))