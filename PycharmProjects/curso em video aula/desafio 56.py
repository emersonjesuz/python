n = ''
somaidade = 0
mediaidade = 0
mediadohomem = 0
nomemasvelho = ''
totmulher20 = 0
for p in range(1,5):
    print('{:-> 20} °ALUNO {:->20}'.format(p,n))
    nome = str(input('NOME : '))
    idade = int(input('IDADE : '))
    sexo = str(input('[F/M] :')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        mediadohomem = idade
        nomemasvelho = nome
    if sexo in 'Mm' and idade > mediadohomem:
        mediadohomem = idade
        nomemasvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade=(somaidade + idade)/4      # a media e dividida pelo tanto de objetos = no caso em 4 idades, /4
print('a media de idade do grupo é \033[33m{}\033[m'.format(mediaidade))
print('o homem mas velho tem \033[33m{}\033[m anos  e se chama \033[33m{}\033[m '.format(mediadohomem, nomemasvelho))
print('temos \033[33m{}\033[m mulheres com menos de 20 anos '.format(totmulher20))