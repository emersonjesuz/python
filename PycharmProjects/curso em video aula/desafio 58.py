from random import randint
computador = randint(0, 10)
print('sou seu computador . . . acabei de pensa em um numero entre 0 e 10')
print('sera que você consegue advinha ?')
total = 0
opiniao = 0
palpites2 = 0
palpites = 0
jogador = 0
tentativa = 0
continua = ''
while computador != jogador:
    computador = randint(0, 10)
    jogador = int(input(' seu palpite:'))
    palpites += 1
    print('errou tente novamente!')
    if computador == jogador:
        print('acertou ')
print('computador jogou {}\n e jogador  jogou {}'.format(computador, jogador))
print('suas tentativas erradas foram {}'.format(palpites))
continua = str(input('deseja ir para a segunda rodada ? [S/N]')).strip().upper()[0]
if continua in 'sS':
    print('VOCÊ GOSTOU MESMO EM !')

if continua in 'nN':
    opiniao = str(input('gostou da experiencia ?'))
    print('\033[31mOBRIGADO POR JOGA !!!\033[m')
total = palpites+palpites2
if total <= 10:
    print('\033[31mVOCÊ È MUITO BOM !')
elif total <= 20:
    print('\033[33mVOCÊ FOI RAZUAVEL!')
else:
    print('VOCÊ PRECISA DE MAS SORTE !')
print('foram um total de {} tentativas '.format(total))
