galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade')))
    galera.append(dado[:]) # assim vc faz uma copia de dados pra galera
    dado.clear()  # clear vai apagar dados

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade .')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores de idade.')