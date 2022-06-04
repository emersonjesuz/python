from time import  sleep
from random import randint
itens=('pedra','papel', 'tesoura')
computador= randint(0,2)
print('-$-'*13)
print(' {:=^39} '.format(" JOKENPÔ "))
print('-$-'*13,'\n')
print('''[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input(' qual você escolhe?'))
if jogador>=3:
    print('\033[31mJOGADA INVALIDA TENTE NOVAMENTE!!!\033[m')
    jogador = int(input(' qual você escolhe?'))
    if jogador>=3:
        print('você ta jogando errado \n')
        print('\033[33mVOU TE PARA !!!')
        sleep(2)
        print(' VOCE TA TODO ERRADO CARA!!!{}'.format())
print('-$-'*13,'\n')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-$-'*13,'\n')
print('COMPUTADOR JOGOU:\033[34m{}\033[m '.format(itens[computador]))
print('JOGADOR JOGOU:\033[34m{}\033[m'.format(itens[jogador]))
sleep(1)
print('-$-'*13)
if computador == 0:     # computador jogou papel
    if jogador==0:
        print('\033[33mEMPATOU')
    elif jogador == 1:
        print('\033[33mJOGADOR VENCEU')
    elif jogador == 2:
        print('\033[33mCOMPUTADOR VENCEU')
    else:
        print('\033[33mJOGADA INVALIDA')
elif computador == 1:   # computador jogou tesoura
    if jogador==0:
        print('\033[33mCOMPUTADOR VENCEU ')
    elif jogador == 1:
        print('\033[33mEMPATOU')
    elif jogador == 2:
        print('\033[33mJOGADOR VENCEU')
    else:
        print('\033[33mJOGADA INVALIDA ')
elif computador == 2:    #computador jogou pedra
    if jogador == 0:
        print('\033[33mJOGADOR VENCEU')
    elif jogador == 1:
        print('\033[33mCOMPUTADOR VENCEU ')
    elif jogador == 2:
        print('\033[33mEMPATE')
    else:
        print('\033[33mJOGADA INVALIDA ')
print('\033[m-$-'*13)
