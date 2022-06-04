frase= ('  ola mundo, aqui da terra esta tudo bem   ')
print(frase.count('a'))
print(frase.upper().count('a'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('mundo','largaticha')) # usando assim nao tem como muda a palavra exatamente
print(frase)
#frase=frase.replace('mundo','largaticha') # mas assim ela salve na memoria  a palvra
print(frase)
print('terra' in frase)
print(frase.split())
dividido=frase.split()
print(dividido[:1])
print(dividido[1][3]) # usando a segundo cochete ele procura a letra na palavra escolhida