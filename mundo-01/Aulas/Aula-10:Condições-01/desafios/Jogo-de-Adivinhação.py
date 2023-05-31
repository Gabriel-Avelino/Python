import random
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

num = random.randint(0, 5)
palpite = int(input('Digite um número entre 0 e 5: '))

if palpite == num:
    print('{1}Parabéns! O número pensado foi o {2}{0}{1}! Você acertou!{3}'.format(num, cores['verde'], cores['amarelo'], cores['limpa']))
else:
    print('{1}Que pena! O número em que pensei era o {2}{0}{3}'.format(num, cores['vermelho'], cores['amarelo'], cores['limpa']))
