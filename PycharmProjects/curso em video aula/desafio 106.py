def sistemadeajuda(item):
    print('\033[7:36:40m')
    help(f'{item}')
    print('\033[m', end='')


while True:
    print('\033[7:30:41m~' * 40)
    print('SISTEMA DE AJUDA PYHELP')
    print('\033[7:30:41m~' * 40)
    print('\033[m', end='')
    n = str(input('FUNÇÃO OU BIBLIOTECA > '))
    if n == 'fim':
        break
    print('\033[7:35:40m~' * 40)
    print(f'ACESSANDO O MANUAL DE {n}')
    print('\033[7:35:40m~' * 40)
    sistemadeajuda(n)
print('\033[7:31m~' * 40)
print('\033[7:31m Programa finalizando \n volte sempre!!!')
print('\033[7:31m~' * 40)