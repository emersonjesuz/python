tupla = (('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.00, 'estojo', 25.00, 'trasferidor', 4.20,
          'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90))
print('-'*42)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*42)
#print(f'''{tupla[0]}...........................R$   {tupla[1]}
#{tupla[2]}........................R$   {tupla[3]}
#{tupla[4]}.........................R$   {tupla[5]}
#{tupla[6]}..........................R$   {tupla[7]}
#{tupla[8]}.....................R$   {tupla[9]}
#{tupla[10]}........................R$   {tupla[11]}      # como eu fiz
#{tupla[12]}.........................R$   {tupla[13]}
#{tupla[14]}.........................R$   {tupla[15]}
#{tupla[16]}...........................R$   {tupla[17]}''')
#print('-'*42)

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')  # como o professor fez
    if pos % 2 == 1:
        print(f'R${tupla[pos]:>7.2f}')
print('-'*42)
