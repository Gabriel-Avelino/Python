num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

if num1 > num2 > num3:
    print('{1}O maior número é {2}{0}{3}'.format(num1, cores['verde'], cores['amarelo'], cores['limpa']))
elif num2 > num1 > num3:
    print('{1}O maior número é {2}{0}{3}'.format(num2, cores['verde'], cores['amarelo'], cores['limpa']))
else:
    print('{1}O maior número é {2}{0}{3}'.format(num3, cores['verde'], cores['amarelo'], cores['limpa']))

if num1 < num2 < num3:
    print('{1}O menor número é {2}{0}{3}'.format(num1, cores['vermelho'], cores['amarelo'], cores['limpa']))
elif num2 < num1 < num3:
    print('{1}O menor número é {2}{0}{3}'.format(num2, cores['vermelho'], cores['amarelo'], cores['limpa']))
else:
    print('{1}O menor número é {2}{0}{3}'.format(num3, cores['vermelho'], cores['amarelo'], cores['limpa']))
