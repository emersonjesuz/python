n = soma = cont = 0
n = int(input('digite um numero [999 para parar] :'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('digite um numero  [999 para parar] :'))
print('são {} numeros digitados e a soma entre todos eles  é {}'.format(cont, soma))


