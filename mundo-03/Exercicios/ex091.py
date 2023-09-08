from random import randint
from time import sleep
from operator import itemgetter
resultados = dict()
ranking = dict()

for c in range(1, 5):
    resultados[f'jogador {c}'] = randint(1, 6)

print('Valores Sorteados: ')
for k, v in resultados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)

print('  == RANKING DE JOGADORES ==')
for i, value in enumerate(ranking):
    print(f'   {i + 1}º lugar: {value[0]} com {value[1]}')
    sleep(1)
