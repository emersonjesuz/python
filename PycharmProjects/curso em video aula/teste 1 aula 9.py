frase='curso em video python'
frase[9:13]
print(frase)
len(frase) # compriento da frase
frase.count('o') #  count vai contar quantas letras tem em ()
frase.find('deo') # vai conta quando começou , deo
'curso' in frase    #   (in) vai pergunta se isso existe em frase
frase.replace('python','android') # replace e igual a substituir, tira python e colocar android
frase.upper()  # vai colocar tudo que é igual a frase em maiusculo
frase.lower()  # vai colocar tudo em minusculo
frase.capitalize() # vai colocar tudo em minusculo mas so a primeira letra da frase fica em maiuscula
frase.title() # vai contar quantas palavras tem e colocar a primeira letra de cada em maiusculo
frase.strip() # vai remover os espaços do inicio da frase e do final
frase.rstrip() # com a adisão do ' r de direita  ' no final da strip ela vai apagar o espaço so da direita
frase.lstrip() # que faz a mesma coisa so que 'l' representa  esquerda assim apaga os espaços so da esquerda
frase.split() # ele vai fazer uma no lista separando cada palavra em uma nova lista
'-'.join(frase) # vai junta as lista que estao separadas
