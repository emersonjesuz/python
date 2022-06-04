def notas(*num, sit=False):
    """
    -> função para analisar as notas dos alunos
    :param num: notas de cada aluno
    :param sit: a situação de cada aluno
    :return: vai retornar cada a valor
    """
    cardeneta = dict()
    cardeneta['total'] = len(num)
    cardeneta['maior'] = max(num)
    cardeneta['menor'] = min(num)
    cardeneta['media'] = sum(num)/len(num)
    if sit:
        if cardeneta['media'] >= 7:
            situa = 'BOA'
        elif cardeneta['media'] >= 5:
            situa = 'RASUAVEL'
        else:
            situa = 'RUIM'
        cardeneta['situação'] = situa
    return cardeneta


print('-' * 30)
n = notas(5.5, 5, 2, sit=True)
for k, v in n.items():
    print(f'{k} é igual a {v}')
help(notas)
