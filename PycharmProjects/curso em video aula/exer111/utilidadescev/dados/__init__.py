def leiaDinheiro(v):
    valido = False
    while not valido:
        total = str(input(f'{v}')).replace(',', '.').strip()
        if total.isalpha() or total == '':
            print(f'\033[31mERRO" {total} NÂO é um preço invalido\033[m')
        else:
            valido = True
            return float(total)


def leiaInt(num):
    while True:
        try:
            total = int(input(f'{num}'))
        except (TypeError, ValueError):
            print('\033[31m ERRO!! DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO USUARIO FECHOU O PROGRAMA ! ')
            return '\033[31mPROGRAMA INTERROPIDO'
        else:
            return total


def leiaFloat(msg):
    while True:
        try:
            total = float(input(f'{msg}'))
        except (TypeError, ValueError):
            print('\033[31m ERRO!! DIGITE UM NUMERO FLOTUANTE  VALIDO.\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO USUARIO FECHOU O PROGRAMA !!')
            return '\033[31mPROGRAMA INTERROPIDO'
        else:
            return total

