
ano=int(input('digite um ano :'))
if ano%4==0 and ano%100!=0 or ano % 400==0:
    print(' o ano {} é um ano BISSEXTO'.format(ano))    # esse programa ler se o ano é ou nao BISSEXTO
else:
    print('o ano {} nao é um ano BISSEXTO'.format(ano))

    from datetime import date
ano1 = int(input('qual o ano que você quer saber ? digite 0 para saber o ano atual '))
if ano1==0:
    ano1= date.today().year
if ano1 % 4==0 and ano1 % 100==0 != 0  or ano1 % 400 == 0:# biblioteca 'datetime' date pra usar a data atual
    print('o ano {} é um ano BISSEXTO'.format(ano1))
else:
    print('o ano {} nao é um ano BISSEXTO'.format(ano1))
