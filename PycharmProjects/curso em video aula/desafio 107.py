from exer111.utilidadescev import moeda
p = float(input('digite um preço: R$'))    # exercicio feito usando um modulo criado
print(f'A mentade de {p} é {moeda.metade(p)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {p} fica {moeda.aumentar(p, 10)}')
print(f'Diminuido 13% de {p} fica {moeda.diminuir(p, 13)}')
