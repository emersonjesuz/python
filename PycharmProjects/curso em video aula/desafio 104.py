def leiaint(num):
    while True:
        total = str(input(f'{num}'))
        if total.isalpha():
            print('\033[31m ERRO!! DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
        elif total.isnumeric():
            total = int(total)
            break
        else:
            print('\033[31m ERRO!! DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
    return total


print('-' * 30)
n = leiaint('digite um numero :')
print(f'você acabou  digitar o numero {n}')
