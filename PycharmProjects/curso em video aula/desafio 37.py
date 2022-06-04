numero = int(input('digite um numero:'))
print('você quer seu numero em :')
print('[\033[33m1\033[m] para BINARIO')
print('[\033[33m2\033[m] para octal')
print('[\033[33m3\033[m] para hexadecimal')
opçao = int(input('digite sua opção:'))
if opçao== 1:
    print(' {} em BINARIO É :\033[34m {}\033[m'.format(numero,bin(numero)[2:]))
elif opçao == 2:
    print('{} em OCTAL É:\033[34m {}\033[mm'.format(numero,oct(numero)[2:]))
elif opçao == 3:
    print('{} em HEXODECIMAL É: \033[34m{}\033[m'.format(numero,hex(numero)[2:]))
else:
    print('\033[31mopção invalida, tente novamente!\033[m')
