soma = 0
cont = 0
for c in range(1,7):
    n1 = int(input('digite o {} valor: '.format(c)))
    if n1 % 2 == 0:  # programa se ler se o numero é par e a soma entre eles
        soma += n1
        cont += 1
print('você informou {} pares e a soma deles  foi {}  '.format(cont,soma))


