from random import randint

num = randint(0, 5)
print('-=-' * 30, '\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n', '-=-' * 30)

palpite = int(input('Em que número pensei? '))
print('PROCESSANDO...')
if num == palpite:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num, palpite))