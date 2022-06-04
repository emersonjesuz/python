def linhas():
    print('-' * 40)


def medida(a, b):
    s = a * b
    print(f'A area de um terreno {a}X{b} = {s}m2')


print(f'{"CONTROLE DE TERRENOS":.^40}')
linhas()
largura = float(input('LARGURA (m) :'))
comprimento = float(input('COMPRIMENTO (m) :'))
medida(a=largura, b=comprimento)
