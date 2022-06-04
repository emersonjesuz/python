tempo=int(input('quanto tempo tem seu carro:'))
if tempo<=3:
    print('carro novo')        # (if) e (else) sao condições que determina ações
else:
    print('carro velho')   # tanto if quanto else precisam de (:) pra da certo
print('--FIM--')

print('carro novo'if tempo<=5 else'carro novo')  # forma mas simplificada porem mas difil de ler
print('--FIM--')