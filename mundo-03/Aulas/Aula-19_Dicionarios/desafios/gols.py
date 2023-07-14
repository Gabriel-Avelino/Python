jogador = {}
gols = []
total = 0

jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
quantidade = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, quantidade):
    partida = int(input(f'Quantos gols na partida {c + 1}? '))
    gols.append(partida)
jogador['gols'] = gols

for g in gols:
    total += g
jogador['total de gols'] = total

print('-=' * 35)
print(jogador)
print('-=' * 35)

for k, v in jogador.items():
    print(f'{k.title()}: {v}')

print('-=' * 35)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, p in enumerate(jogador['gols']):
    print(f'    => Na partida {i + 1}, fez {p} gols.')
print(f'Foi um total de {jogador["total de gols"]} gols.')
