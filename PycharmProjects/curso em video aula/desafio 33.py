n1 = int(input(' digite um valor: '))
n2 = int(input('digite outro valor: '))
n3 = int(input(' mas um valor: '))

if n1<n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:    # programa pra ler o numero maior e menor
    menor= n2
if n3< n1 and n3 < n2:
    menor= n3
#
if n1 > n2 and n1 > n3 :
    maior = n1
if n2 > n1 and n2 > n3:
    maior=n2
if n3 > n1 and n3 > n2 :
    maior = n3
print('o numero maior é {} e o numero menor é {}'.format(maior,menor))