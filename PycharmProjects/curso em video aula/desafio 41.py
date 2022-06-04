idade = int(input('qual a ano você nasceu?'))
from datetime import date
ano=date.today().year
total= ano - idade
if idade <=9:
    print('o atleta tem :{}anos \n categoria : \033[33mMIRIM\033[m'.format(total))
elif idade >9 and idade <=14:
    print('o atleta tem : {}anos \n categoria : \033[33m INFANTIL \033[m'.format(total))
elif idade >14 and idade<=19:
    print('o atleta tem : {} anos \n categoria: \033[33mJUNIOR\033[m'.format(total))
elif idade > 19 and idade < 21:
    print('o atleta tem : {} anos \n categoria : \033[33mSENIOR\033[m'.format(total))
elif idade >= 21:
    print('o atleta tem : {} anos  \n categoria : \033[33mMASTER\033[m'.format(total))
