ficha = []
while True:
    alunos = str(input('NOME:'))
    n1 = float(input('NOTA1:'))
    n2 = float(input('NOTA2:'))
    media = (n1 + n2)/2
    ficha.append([alunos, [n1, n2], media])
    opc = str(input('QUER CONTINUA? [S/N]')).strip().upper()[0]
    if opc == "N":
        break
print('=-'*30)
print(f'{"NO.":<4} {"NOME":<10}  {"MEDIA":>8}')
for i, l in enumerate(ficha):
    print(f'{i:<4} {l[0]:<10} {l[2]:>8.1f}')
print('=-'*30)
while True:
    al = int(input('Qual o numero do aluno você quer saber a nota [999] encerra o programa ! '))
    if al == 999:
        print('Finalizando. . .')
        break
    if al <= len(ficha) - 1:
        print(f'as notas de {ficha[al][0]} são {ficha[al][1]}')
        print('-='*30)
print('<<< VOLTE SEMPRE >>>')