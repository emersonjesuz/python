from datetime import date
cadastro = {}
cadastro['NOME'] = str(input('NOME:')).upper()
ano = int(input('ANO DE NASCIMENTO:'))
dataatual = date.today().year
cadastro['IDADE'] =idade = dataatual - ano
cadastro['CTPS'] = int(input('CARTEIRA DE TRABALHO (0 NÃO TEM):'))
if cadastro['CTPS'] == 0:
    print('-=' * 30)
    for k, v in cadastro.items():
        print(f' - {k} te valor {v}')
else:
    cadastro['CONTRATO'] = int(input('ANO DE CONTRATAÇÃO:'))
    cadastro['SALARIO'] = float(input('SALARIO : $'))
    cadastro['APOSENTADORIA'] = cadastro['IDADE'] + ((cadastro['CONTRATO'] + 35) - dataatual)
    print('-=' * 30)
    for k, v in cadastro.items():
        print(f' - {k} Tem o valor {v}')
