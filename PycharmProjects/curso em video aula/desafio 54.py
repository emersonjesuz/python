from datetime import date
cont = 0
cont1 = 0
for c in range(1, 8):
    nome = int(input('{}]\033[34mdigite qual o ano de nascimento:\033[m '.format(c)))
    data = date.today().year
    tudo = data - nome
    if tudo >= 21:
        cont += 1
    else:
        cont1 += 1
print('{} \033[33mpessoas são maiores de 21 anos\033[m\n{} \033[33mpessoas ainda vão fazer 21anos '.format(cont, cont1))
