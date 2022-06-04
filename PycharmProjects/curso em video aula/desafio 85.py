total = []  # colocando duas listas dentro de um unica lista e separando se eles são impares ou par
impar = []  # [[], []] isso serve pr coloar duas listra em uma ja direto
par = []
for c in range(1, 8):
    valor = int(input(f'digite o {c}°. valor  : '))
    if valor % 2 == 0:
        par.append(valor)
        par.sort()

    if valor % 2 == 1:
        impar.append(valor)
        impar.sort()

total.append(par)
total.append(impar)

print(f'os valores pares digitados foram :{total[0]}')
print(f'os valores impares digitados foram :{total[1]}')
