def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
# funçoes usando retorno serve pra podermos personalisar usando variavel


n1 = soma(2, 4, 6)
n2 = soma(2, 10)
n3 = soma(100)
print(f'a soma entre os valores são {n1} e {n2} e {n3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#n = int(input('digite um numero!'))
#print(f'fatorial de {n} é igual a {fatorial(n)}')
r1 = fatorial(9)
r2 = fatorial(4)
r3 = fatorial()
print(f'os resultados são {r1}, {r2} e {r3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('qual valor você escolhe ??'))
if par(num):
    print('È PAR')
else:
    print('È IMPAR')
