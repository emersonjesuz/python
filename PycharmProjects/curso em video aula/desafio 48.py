c = 0  # isso e um acumulador
cont = 0 # isso é um contador
for num in range(1,501, 2):
    if num % 3 == 0:
        cont = cont+1  # isso é a forma de um contador
        c = c + num  # forma de acumulador
print(' a soma de todos os {} valores é {}'.format(cont, c))
