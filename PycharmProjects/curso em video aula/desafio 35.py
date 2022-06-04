print('-=-'* 20)
print(' ANALISADOR DE TRIANGULO  ')
print('-=-'*20)                         # complemento ta no desafio 45
r1 = float(input('primeiro segmento:'))
r2 = float(input('segundo segmento:'))    # se pode ou não forma um triangulo
r3 = float(input('terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima PODEM FORMA triangulo')
else:
    print("os segmentos acima NÂO PODEM FORMA triangulo ")
