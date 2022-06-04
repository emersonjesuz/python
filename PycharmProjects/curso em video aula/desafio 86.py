lista = [[], [], []]
t1 = n1 = valor = 0
for t in range(0, 3):
    t1 = int(input(f'digite um valor para [0, {t}] :'))
    lista[0].append(t1)
    lista[0].sort()
for p in range(0, 3):
    n1 = int(input(f'digite um valor para [1, {p}] :'))
    lista[1].append(n1)
    lista[1].sort()
for d in range(0, 3):
    valor = int(input(f'digite um valor para [2, {d}] :'))
    lista[2].append(valor)
    lista[2].sort()
   # minha formula == so que da trabalho pra deixa tudo alinhado
print('=-'*30)
print(f'[ { lista[0][0] } ][ { lista[0][1] } ][ { lista[0][2] } ]')
print(f'[ { lista[1][0] } ][ { lista[1][1] } ][ { lista[1][2] } ]')
print(f'[ { lista[2][0] } ][ { lista[2][1] } ][ { lista[2][2] } ]')
print('=-'*30)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # dessa forma a lista ja vai mstra como ela vai ser preenchido
for l in range(0, 3):
    for c in range(0, 3): # usando um laço dentro do outro para cobrir 3 linhas deitadas e 3 linhas em pé
        matriz[l][c] = int(input(f'digite um valor para [{l},{c}] :'))
print('=-'*30) # tem como criar uma variavel lista usar varios contadores
for l in range(0, 3):
    for c in range(0, 3): # usando  o laço for pra criar 3 linhas deitadas e 3 linhas em pé
        print(f'[{matriz[l][c]:^5}]', end=' ') # para fazer a caixar ficarem do msm tamanho :^5 isso vai centralisa em 5 espaços
    print() # usando o print dessa forma qundo ela termina as 3 vezes do primeiro laço , ela quebra a linha e assim o laço segue na seguencia pra mas 3
