
soma = str(input('VAMOS DE NOVO ? [SIM/ NÂO]'))
while soma not in 'naoNAO':
    computador = randint(1,10)
    print('COMPUTADOR JOGOU : {}'.format(computador))
    print('JOGADOR JOGOU: {}'.format(jogador))
    derrota = int(input('VOCÊ ERROU! tente novamente\n escola um numero !'))
    if computador == jogador:
        print('VOCÊ VENCEU NOVAMENTE !')
        print('eu joguei {}'.format(computador))
        total = erro + erro1
        print('1° rodada você errou um total de {}'.format(erro))
        print('2° rodada você errou um total de {}'.format(erro1))
        print('ERROS NO TOTAL\n'.format(total))
        print('NÃO JOGO MAS, VOCÊ É MUITO BOM ')
if soma in 'naoNAO':
    print('OBRIGADO POR JOGA !\n total de erros: {}'.format(erro))
