from exer111.utilidadescev import moeda
p = float(input('Digite o peço do produto : R$'))
print(f'a metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'o aumento de 10% de {moeda.moeda(moeda.aumentar(p, 10))}')