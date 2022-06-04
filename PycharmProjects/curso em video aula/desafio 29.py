from time import  sleep
velocidade = float (input('qual a sua velocidde?'))
multa=(velocidade-80)*7.00
print('PROCESSANDO . . .')
sleep(3)
if velocidade<=80:
    print('sua velocidade esta pelo permitido! CONTINUE EM SEGUNRAÇA!')
else:
    print('VOCE FOI MULTADO !')
    sleep(2)
    print('PROCESSANDO SUA VELOCIDADE . . .')
    sleep(2)
    print('VOCE EXEDEU O LIMITE PERMITDO DE 80,00KM ')
    sleep(2)
    print('sua velocidade é {:.2f}KM '.format(velocidade))
    sleep(1)
    print('ESTAMOS CALCULANDO SUA MULTA . . .')
    sleep(3)
    print(' VALOR ATUAL {:.2f}R$ DA MULTA !'.format(multa))
