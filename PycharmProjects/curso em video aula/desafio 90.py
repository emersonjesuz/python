registro = dict()
registro['NOME'] = str(input('NOME:')).upper()
registro['MEDIA'] = float(input(f'A MEDIA DE {registro["NOME"]}:'))
if registro['MEDIA'] >= 7:
    registro['SITUAÇÂO'] = 'APROVADO'
elif 5 <= registro['MEDIA'] < 7:
    registro['SITUAÇÂO'] = 'RECUPERAÇÃO'
else:
    registro['SITUAÇÂO'] = 'REPROVADO'
print('- -'*20)
for t, a in registro.items():
    print(f' - {t} igual a {a}')
