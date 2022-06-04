n = soma = cont = maior = media = 0
menor = 0
para = ''
# resp = 'S'    uma variavel
# while resp in 'Ss'     uma forma de fazer uma while com letra
while para != 'N':
    soma += n
    cont += 1
    n = int(input('digite um valor '))
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    para = str(input('deseja continua [SIM] [NAO]')).strip().upper()[0]
media = soma/ cont
print('''maior numero {}
menor numero {}
a media entre eles é {:.1f}'''. format(maior, menor, media))

