from time import sleep
def primeiraslista():
    print('-' * 40)
    print('Contagem de 1 ate 10  de 1 em 1 ')
    for c in range(1, 11, 1):
        print(c, end=' ')
        sleep(0.5)
    print('FIM')
    print('-' * 40)
    print('Contagem de 10 ate 0 de 2 em 2 ')
    for c in range(10, 0 - 1, -2):
        print(c, end=' ')
        sleep(0.5)
    print('FIM')
    print('-' * 40)



def tentativa(inicio, fim, pulo):
    print(f'Contagem de {lista[0]} ate {lista[1]} de {lista[2]} em {lista[2]}')
    if pulo < 0:
        pulo *= -1
    if fim < inicio:
        fim = fim - 1
    if inicio > fim and pulo >= 1:
        for c in range(inicio, fim, -pulo):
            print(c, end=' ')
            sleep(1)
        print('FIM')
    elif inicio < fim and pulo >= 1:
        for c in range(inicio, fim, pulo):
            print(c, end=' ')
            sleep(1)
        print('FIM')
    elif pulo == 0 and inicio > fim:
        for c in range(inicio, fim, -1):
            print(c, end=' ')
            sleep(1)
        print('FIM')
    elif pulo == 0:
        for c in range(inicio, fim):
            print(c, end=' ')
            sleep(1)
        print('FIM')


lista = []
primeiraslista()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('INICIO : '))
fim = int(input('FIM : '))
pulo = int(input('PASSO : '))
lista.append(inicio)
lista.append(fim)
lista.append(pulo)
tentativa(lista[0], lista[1], lista[2])
print('-' * 40)
