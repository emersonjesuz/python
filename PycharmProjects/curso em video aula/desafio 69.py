sexo = opçao = ' '
idade = mulhercont = homecont = soma = cont = menor = 0

while True:
    print('..' * 30)
    print('CADASTRE UMA PESSOA')
    print('..' * 30)
    idade = int(input('idade :'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [ M / F ] ')).strip().upper()[0]
        print('..'*30)

    if sexo == 'M':
        homecont += 1

    elif sexo == 'F':
        mulhercont += 1
        if idade < 20:
            menor += 1

    if idade > 18:
        cont += 1
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('deseja prosseguir ? [S / N]')).strip().upper()[0]
    if opçao == 'N':
        break
print(f'tem {cont} pessoa maior de 18 anos ')
print(f'foram {homecont} homem e {mulhercont} mulher  ')
print(f'tem  {menor} mulher menor de 18 anos ')
