contmaior = 0
contmenor = 0
                          # programa pra ler qual a maior e o menor peso entre 5 pessoas
maior = 0
menor = 0         # adicionei um programa de contidade pra ler quantas pessoas tem acima ou abaixo  de 50kg
for c in range(1, 6):
    peso = float(input('qual o {}° peso :'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    #
    if peso >= 50:
        contmaior += 1 # contidade maior
    #
    else:
        #
        contmenor += 1  # contidade menor
        #
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso é {}kg'.format(maior))
print('o menor peso é {}kg'.format(menor))
print('são {} de pessoas acima do peso '.format(contmaior))
print('são {} de pessoas abaixo do peso '.format(contmenor))


