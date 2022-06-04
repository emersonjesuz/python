peso = float(input('digite seu peso:'))
altura = float(input('digite sua altura:'))
imc = peso/altura**2
if imc <= 18.5:
    print('seu status de imc: {:.1f} \n \033[33m você esta abaixo do peso!'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('seu status de imc: {:.1f} \n \033[33m você esta no peso ideal!'.format(imc))
elif imc > 25 and imc <= 30 :
    print('seu status de imc: {:.1f} \n \033[33m você esta sobrepeso!'.format(imc))
elif imc > 30 and imc <= 40:
    print('seu status de imc: {:.1f} \n \033[33m você esta com obesidade!'.format(imc))
elif imc > 40:
    print('seu status de imc: {:.1f} \n \033[33m você esta com obesidade morbida! '. format(imc))
