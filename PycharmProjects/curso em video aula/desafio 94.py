lista = []
planilha = {}
media = soma = 0
while True:
    planilha.clear()
    planilha['nome'] = str(input('nome : '))
    while True:
        planilha['sexo'] = str(input('sexo: [M/F] ')).upper()[0].strip()
        if planilha['sexo'] in 'MF':
            break
        print('erro, REPOSPONDA APENAS M OU F !')
    planilha['idade'] = int(input('idade : '))
    soma += planilha['idade']
    lista.append(planilha.copy())
    while True:
        opc = str(input('Deseja continua [S/N] :')).strip().upper()[0]
        if opc in 'SN':
            break
        print('erro!, RESPONDA APENAS S OU N !')
    if opc == 'N':
        break
print('-=' * 30)
print(f'   - o Grupo tem {len(lista)} pessoas ')
media = soma / len(lista)
print(f'   - a media de idade é de {media:5.2f} anos. ')
print('   - As mulheres cadastradas são: ', end=' ')
for p in lista:
    if p['sexo'] in "F":
        print(f'{p["nome"]},', end=' ')
print()
print('  - lista das pessoas que estão acima da media ! ')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'  {k} = {v}', end='  ')
        print()
print('    >>> ENCERRADO <<<')
