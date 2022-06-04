def dobra(lista):
    pos = 0
    while pos < len(lista):    # dessa forma ele vai dobra os valores da lista usando uma função criada pelo def
        lista[pos] *= 2
        pos += 1


valores = [4, 5, 1, 8, 10]   # para a função ler a lista tem que criar uma lista e colocar na função desejada
dobra(valores)
print(valores)
