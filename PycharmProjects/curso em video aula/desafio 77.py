palavras = ('arame', 'pedra', 'caneta', 'sofa', 'cenoura', 'sola', 'peixe',
            'safada', 'arco', 'cachoeira', 'material')
for p in palavras:
    print(f'\n \033[mna palavra \033[33m{p.upper()}\033[m temos\033[34m ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

        # cada palavra de uma tuplei vira uma list de palavras