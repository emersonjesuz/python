print('\033[31m-=-\033[m'*20)    # forma de triangulo #2#
print('ANALISADOR DE TRIANGULOS')
print(('\033[31m-=-\033[m'*20))
n1 = float(input('primeiro segmento:'))  # != e diferente na programação
n2 = float(input('segundo segmento'))    #  == e igual na programaçao
n3 = float(input('terceiro segmento'))   # if pode ser usado dentro de if
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('pode forma um triangulo ',end=' ')
    if  n1 == n2 == n3:
        print('\033[33mEQUILATERO!')
    elif n1 != n2 != n3 != n1:
        print('\033[33mESCALENO!')
    else:
        print('\033[33mISOSCELES!')

else:
    print('\033[31mnao forma  um triangulo ')