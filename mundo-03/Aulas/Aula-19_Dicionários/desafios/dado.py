from random import randint
from time import sleep
resultados = {}

for c in range(0, 4):
    resultados[f'jogador {c + 1}'] = randint(1, 6)

print('Valores Sorteados:')
for k, v in resultados.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

print('Ranking dos Jogadores:')
for i, e in enumerate(sorted(resultados, key=resultados.get, reverse=True)):
    print(f'    {i + 1}º lugar: {e} com {resultados[e]}')
    sleep(1)
