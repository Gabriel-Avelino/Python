jogador = dict()
gols = []
jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
quantidade = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, quantidade):
    gols.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
jogador['gols'] = gols[:]
gols.clear()
jogador['total'] = sum(jogador['gols'])

print('-=' * 30)
print(jogador)

print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'    => Na partida {i + 1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
