pa = int(input('qual o PA:'))
ra = int(input('qual a razão:'))
dec = pa + (10-1)*ra # calculo de uma PA
for c in range(pa, dec + ra, ra):
    print('{}'.format(c), end='-')
print('acabou')
print(dec)