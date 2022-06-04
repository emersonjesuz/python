def voto(idade):
    from datetime import date
    anoatual = date.today().year
    aps = anoatual - idade
    print(f'{aps} Anos ', end=' ')
    if aps < 16:
        return print('AINDA NÃO VOTA!')
    if 15 < aps < 18:
        print(' VOTO OPCIONAL')
    if aps >= 18:
        return print('VOTO OBRIGATORIO !')
    if aps >= 65:
        return print('VOTO OPCIONAL ')


print('-' * 30)
n = int(input('Qual o ano do nascimento ?'))
voto(n)
