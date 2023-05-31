num = int(input('Digite um número: '))
ant = num - 1
suces = num + 1
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

print('O antecessor de {}{}{} é {}{}{}, \ne o sucessor é {}{}{}'.format(cores['amarelo'], num, cores['limpa'], cores['vermelho'], ant, cores['limpa'], cores['verde'], suces, cores['limpa']))
