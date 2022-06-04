valor = 1
cont = 3
numero = 0
total = 0
soma = 0
print('-'*35)
print('sequência de fibonacci')
print('-'*35)
n = int(input('quantos termos você quer mostra ?'))
while cont <= n:
    cont += 1
    total = numero + valor
    numero = valor                # como criar uma seguencia contando
    valor = total
    print('{} > '.format(total), end='')
print(' FIM')
print('~'*35 )
