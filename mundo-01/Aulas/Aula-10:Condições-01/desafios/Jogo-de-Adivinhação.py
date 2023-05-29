import random

num = random.randint(0, 5)
palpite = int(input('Digite um número entre 0 e 5: '))

if palpite == num:
    print('Parabéns! O número é {}! Você acertou!'.format(num))
else:
    print('Que pena! O número era {}'.format(num))
