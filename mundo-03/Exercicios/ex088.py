from random import randint
from time import sleep
palpites = []
jogo = []

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

quantidadeJogos = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, quantidadeJogos):
    for i in range(0, 6):
        num = 0
        while num == 0 or num in jogo:
            num = randint(1, 60)
        jogo.append(num)
        jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()

print('-=' * 3, F' SORTEANDO {len(palpites)} JOGOS ', '-=' * 3)
for e, j in enumerate(palpites):
    sleep(1)
    print(f'Jogo {e + 1}: {j}')
print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')
