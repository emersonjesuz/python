# comandos
nome=str(input('qual o seu nome ?'))
if nome=="gustavo":
    print('que nome lindo')
else:
    print('seu nome tão normal ')
print('bom dia, {} '.format(nome))

n1= float(input('digite um numero :'))
n2= float(input('digite outro numero :'))
m=(n1+n2)/2
print('a sua media foi: {:.1f}'.format(m))
if m>=6.0:
    print('sua nmedia foi otima, PARABENS ')

else:
    print('sua media foi ruim, ESTUDE MAS')

