def metade(m=0, f=False):
    """
    -> informa a metade do valor incerido!
    :param m: valor a ser adicionado
    :param f: informa com False ou True se vai adicionar a formataçao pra centavos
    :return:
    """
    tot = m / 2
    return tot if f is False else moeda(tot)
 # a forma como o professor fez<<< retorna tot se (f) é falso se nao retorna moeda (tot)


def dobro(d=0, f=False):
    tot = d * 2
    if f:
        return moeda(tot)
    else:
        return tot


def aumentar(au=0, val=1, f=False):
    tot = au + (au * val / 100)
    if f:
        return moeda(tot)
    else:
        return tot


def diminuir(dim=0, val=1, f=False):    # certo
    tot = dim - (dim * val / 100)
    if f:
        return moeda(tot)
    else:
        return tot


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')  #replace troca uma coisa por outra


def resumo(val=0, au=10, redu=5):
    print('-' * 30)
    print('      RESUMO DO VALOR   ')
    print('-' * 30)
    print(f'preço analisado \t{moeda(val)}')
    print(f'dobro do preço  \t{dobro(val, True)}')
    print(f'metade do preço \t{metade(val, True)}')
    print(f'{au}% de aumento \t\t{aumentar(val, au, True)}')
    print(f'{redu}% de redução \t\t{diminuir(val, redu, True)}')
    print('-' * 30)
