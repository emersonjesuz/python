n = cont = soma = 0
while True:
    n = int(input('digite um numero [999 para parar] : '))
    if n == 999:
        break   # break faz while para
    soma += n
    cont += 1
print(f'a soma entre os {cont} valores foi {soma}')  # nova forma de print sem o .format
