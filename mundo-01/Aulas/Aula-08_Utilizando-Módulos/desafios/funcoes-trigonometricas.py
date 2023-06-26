from math import sin, tan, cos, radians
ang = float(input('Digite o ângulo desejado: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }
print('Seno: {3}{0}{4} \nCosseno: {3}{1}{4} \nTangente: {3}{2}{4}'.format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang)), cores['verde'], cores['limpa']))
