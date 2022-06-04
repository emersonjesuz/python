from exer111.utilidadescev import moeda
p = float(input('informe o preço do produto:'))
print(f'A metade de {moeda.moeda(p)} é de {moeda.metade(p, True)}')
print(f'o dobro de{moeda.moeda(p)} é de {moeda.dobro(p,True)}')
print(f'o aumento de 15% de {moeda.moeda(p)} é de {moeda.aumentar(p, 15, True)}')
print(f'A diminuição de 30% de {moeda.moeda(p)} é de {moeda.diminuir(p, 30, True)}')