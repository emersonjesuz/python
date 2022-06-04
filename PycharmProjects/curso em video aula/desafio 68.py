from random import randint
from time import sleep
escolha = ''
total = valor = soma = compt = impar = par = cont = 0
print('~~'*30)
print('\033[31mOI SOU SEU COMPUTADOR VAMOS BRINCAR DE PAR OU IMPAR?\033[m')
print('~~'*30)
while True:
    compt = randint(1, 10)
    soma = (compt + valor) % 2
    escolha = str(input('qual você escolhe [PAR / IMPAR] : ')).strip().upper()[0]
    valor = int(input('qual numero quer jogar :'))
    total = compt + valor

    if escolha == 'P':
        print(' JOGADOR JOGOU: PAR\nCOMPUTADOR JOGOU:  IMPAR')
        sleep(2)
        if soma == 1:
            print('\033[33mCOMPUTADOR VENCEU \033[m')
            print(f'{total} è par ')
            break
        elif soma == 0:
            print('\033[33mJOGADOR VENCEU\033[m ')
            print(f'{total} è impar ')
            cont += 1

    elif escolha == "I":
        print('JOGADOR JOGOU: IMPAR\nCOMPUTADOR JOGOU: PAR ')
        sleep(2)
        if soma == 1:
            print('\033[33mJOGADOR VENCEU\033[m')
            print(f'{total} è impar')
            cont += 1
        elif soma == 0:
            print('\033[33mCOMPUTADOR VENCEU\033[m')
            print(f'{total} è par ')
            break
    else:
        print('\033[31merro finalizando programa. . .\033[m')
        sleep(2)
        break
    print(f'computador jogou: {compt}\njogador jogou: {valor} ')
print(f'\033[31mGAME OVER !\033[m você ganhou {cont} vez!')
print('\033[34mobrigado por jogar!\033[m')
