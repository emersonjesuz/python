frase = str(input('digite uma frase')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1,-1,-1): # programa que ler se e um palidromo
    inverso += junto[letra]
print(' o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('temos um palidromo ')
else:
    print('não temos um palidromo')


frase1 = str(input('digite a frase')).strip().upper()
palavra1 = frase1.split()
junto1 = ''.join(palavra1)
inverso1 = junto1[::-1]
print('o inverso de {} é {}'.format(junto1,inverso1))
if inverso1 == junto1:
    print('temos um palimidro')
else:
    print('não temos um palimidro ')
    