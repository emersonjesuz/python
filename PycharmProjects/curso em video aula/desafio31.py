# como eu fiz
distancia = float(input('qual a sua distancia ?'))
media = distancia*0.50
maxima = distancia*0.45
if distancia>=200:
    print(' a distancia  é {}Km, o valor a pagar é : {:.2f}R$'.format(distancia,maxima))
else:
    print(' a distancia else é {}Km, o valor a se pagar é : {:.2f}R$'.format(distancia,media))
# como o professor fez
d = float(input('qual a distancia percorrida ?'))
print('a distancia é {}'.format(d))
if d <=200:
    preço=d*0.50
else:
    preço=d*0.45
print('o preço da sua corrida é {:.2f}R$'.format(preço))

de= float(input('digite a sua distancia:'))
print('a sua distancia {}'.format(de))
p= de * 0.50 if de <=200 else de * 0.45
print(' e o preço {:.2f}'.format(p))