nota = float(input('digite sua nota :'))
nota2 = float(input('digite sua segunda nota :'))
b= (nota+nota2)/2

if b < 5.0:
    print('sua media esta baixa !')
    print('\033[31mREPROVADO \033[m \n {}'.format(b))
elif b >= 7.0 and b<=10:
    print('sua media esta alta !')
    print('\033[32mAPROVADO!\033[m\n {:.1f} '.format(b))
elif b>=5.0  and b <=6.9:
    print('sua media nao foi o suficiente')
    print('\033[33mRECUPERAÇÂO!\033[m \n {}'.format(b))
else:
    erro= b > 10
    print('erro tente novamente !')
