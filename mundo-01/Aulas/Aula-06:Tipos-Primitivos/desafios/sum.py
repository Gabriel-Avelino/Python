num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

soma = num1 + num2

print('A soma entre os número {}{}{} e {}{}{} resulta em {}{}{}'.format(cores['amarelo'], num1, cores['limpa'], cores['amarelo'], num2, cores['limpa'], cores['verde'], soma, cores['limpa']))
