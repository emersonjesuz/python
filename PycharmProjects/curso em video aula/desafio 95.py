jogador = dict()
gol = list()
selecionados = []
total = cont = 0
opc = ' '
while True:
    cont = 0
    jogador.clear()
    gol.clear()
    jogador['nome'] = str(input('NOME do jogador :')).upper()
    jogos = int(input(f'quantas partidas {jogador["nome"]} jogou ? '))
    print('--' * 30)
    print(f'     <<< {jogador["nome"]} jogou {jogos} partidas >>> ')
    while cont != jogos:
        cont += 1
        gol.append(int(input(f'quantos gol ele fez no {cont}° jogo : ')))
        jogador['gol'] = gol[:]
        jogador['total'] = sum(gol)
        if cont == jogos:
            break
    selecionados.append(jogador.copy())
    while True:
        print('--' * 30)
        opc = str(input('Se deseja continua [S,N] :')).strip().upper()[0]
        if opc in "SN":
            break
        print('ERRO!! Resposta apenas S ou N ')
    if opc == 'N':
        break
print('--' * 30)
print(' cod', end='')
for k in jogador.keys():
    print(f'{k:>15}', end='')
print()
print('--' * 30)
for i, s in enumerate(selecionados):
    print(f"{i:>3}", end='')
    for v in s.values():
        print(f'{str(v):>15}', end='')
    print()
print('- - ' * 30)
while True:
    opc = int(input('Mostrar dados de qual jogador : '))
    if opc == 999:
        break
    if opc > len(selecionados):
        print(f'Não tem jogador {opc}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {selecionados[opc]["nome"]}')
        for i, v in enumerate(selecionados[opc]['gol']):
            print(f'    No jogo {i+1} Fez {v}')
    print('--' * 30)
print('<<< VOLTE SEMPRE >>>')
