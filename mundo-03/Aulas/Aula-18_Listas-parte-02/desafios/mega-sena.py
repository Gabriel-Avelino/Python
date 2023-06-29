from random import randint
from time import sleep
palpites = []
jogo = []

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

quantidadeJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=-=-= {:^20} -=-=-='.format(f'SORTEANDO {quantidadeJogos} JOGOS '))

for c in range(0, quantidadeJogos):
    i = 0
    while i < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            i += 1
    palpites.append(jogo[:])
    jogo.clear()

for e, j in enumerate(palpites):
    print(f'Jogo {e + 1}: {j}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')
