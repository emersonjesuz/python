estado = dict()  # dict é dicionario
brasil = list()
for c in range(0, 3):
    estado['ESTADO'] = str(input('Estado:')).strip().upper()
    estado['-'] = str(input('Sigla do Estado:')).strip().upper()
    brasil.append(estado.copy()) # usando ".copy()" ele vai copiar o dicionario ( diferente de lista que usamos o [:])
print('=-'*30)
for e in brasil:
    for k, v in e.items():
        print(f' {k} {v}', end=' ')
    print()
print('- -'*20)
