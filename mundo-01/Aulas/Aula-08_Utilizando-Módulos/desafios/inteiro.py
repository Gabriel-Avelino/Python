from math import trunc
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

num = float(input('Digite um número: '))

print('A parte inteira do número {2}{0}{4} é: {3}{1}{4}'.format(num, trunc(num), cores['azul'], cores['verde'], cores['limpa']))
