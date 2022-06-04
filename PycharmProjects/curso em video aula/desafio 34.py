from  time import  sleep
salario=float(input('qual o seu salario?'))
print('PROCESSANDO  . . .')
sleep(2)
if salario<=1250:     # calculo de % pra calcular o valor de aumento ou desconto
    valor=salario+(salario*15)/100
    print(' quem ganhava {:.2f}R$, vai passar a ganhar :'.format(salario))
else:
    valor=salario+(salario*10)/100
    print(' quem ganhava {:.2f}R$, vai passar a ganhar :'.format(salario))
sleep(3)
print('-=-'*20)
print('\033[31msalario atual \033[m: {:.2f}R$ '.format(valor))
print('-=-'*20)