num = int(input('Digite um número: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

if num % 2 == 0:
    print('{1}O número {2}{0}{1} é par.{3}'.format(num, cores['verde'], cores['amarelo'], cores['limpa']))
else:
    print('{1}O número {2}{0}{1} é ímpar.{3}'.format(num, cores['vermelho'], cores['amarelo'], cores['limpa']))
