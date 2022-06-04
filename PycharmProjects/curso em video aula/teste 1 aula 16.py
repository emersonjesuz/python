lanche = ('biscoito', 'maça', 'limão', 'açai', 'carne') # isso é uma tupla / tupla é uma variavel composta !
print(lanche[:3])                           # as tuplas são imutaveis ! tupla é uma variavel com opções !
print(f'eu comprei {lanche[:4]}')
for comida in lanche:
    print(f'eu vou comer {lanche}')
for cont in range(0, len(lanche)):
    print(lanche[cont])  # usando o len ele vai me da quantos itens tem na variavel lanche
                 # mas fazendo um lanche[ cont ]  ele vai colocar cada item na variavel de acordo com cada numero de len
for pos , lanche in enumerate(lanche):
    print(f'eu vou comer {lanche} na posição {pos}')
print(sorted(lanche))  # sorted ele colocar em ordem
a = (2,4,6)
b = (4,6,1)
c = a + b  # se colocar + em duas ou mas tuplas ela nao vai soma ! apenas juntar uma tupla na outra
print(c)
print(c.count(6))  #  count vai dizer quantos coisas expecifica tem na tupla
print(c.index(6))  # index vai me dizer em qual possição esta a coisa expecifica exp: (2) possição 0
pessoa = ('allan', 20,'M', 1.70)   # tem como  colocar numeros e letras na mesma tupla
del (pessoa)  # del deleta qualquer coisa mas na tupla ele so pode deletar ela inteira
