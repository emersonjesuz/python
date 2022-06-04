from datetime import date
num = int(input('digite qual o ano que você nasceu:'))
ano = date.today().year    # programa pra ler se ja passou ou nao do tempo de se alista
data= ano - num
if data < 18 :
    m= 18 - data
    print('\033[33m AINDA VAI SE ALISTAR\033[m')
    print('ainda falta {} anos  para você ir se  alistar '.format(m))
elif data > 18:
    m=data - 18
    print('\033[31mJA PASSOU DO TEMPO\033[m ')
    print('ja passou {} anos  do tempo de se alistar!'.format(m))
else:
    f =data = 18
    print('\033[32mHORA CERTA!\033[m')
    print('você esta na hora certa de se alistar')
