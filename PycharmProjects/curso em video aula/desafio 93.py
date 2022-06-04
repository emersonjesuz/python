jogador = dict()
Gol = []
total = 0
jogador['nome'] = str(input('Nome do jogador :')).upper()
patidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for cont in range(1, patidas + 1):
    gol = int(input(f'quantos gol na partida {cont} : '))
 #   total += gol ~~~~~~~ uma forma de somar o valor que esta em um laço
    Gol.append(gol)
    jogador['Gol'] = Gol
    jogador['total'] = sum(Gol)  # sum vai somar o valor de uma lista
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v} ')
print('-=' * 30)
print(f' o jogador {jogador["nome"]} jogou {patidas} partidas ')
for i, v in enumerate(Gol):
    print(f'    =>  Na partida {i+1}, fez {v} Gols. ')
print(f'foi um Total de {jogador["total"]}.')
