def leiaint(num):
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


def leiafloat(msg):
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


print('-' * 30)
inteiro = leiaint('digite um numero :')
flotuante = leiafloat('Digite um numero')
print(f'você acabou  digitar o numero {inteiro}')
print(f'você informou o numero {flotuante}')
print('-' * 30)
