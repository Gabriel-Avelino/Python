def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


jogador = str(input('Nome do Jogador: ')).strip().title()
num_gols = input('Número de Gols: ')

if not num_gols.isnumeric():
    num_gols = 0
else:
    num_gols = int(num_gols)
if jogador == '':
    print(ficha(gols=num_gols))
else:
    print(ficha(jogador, num_gols))

