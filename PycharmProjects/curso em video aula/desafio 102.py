def fatorial(cont=1, show=False):


    '''
    Fatorial => valor de um numero
    :param cont: valor do fatorial
    :return: vai retorna
    '''

    f = 1
    while cont != 0:
        f *= cont
        if show:
            print(f'{cont}', end=' ')
            if cont > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        cont -= 1
    print(f'{f}')


#fatorial(5, show=True)
help(fatorial)
