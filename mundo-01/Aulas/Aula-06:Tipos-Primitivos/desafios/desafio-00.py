n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m'
         }
# print('A soma entre', n1, 'e', n2, 'vale', s)

print('A soma entre {}{}{} e {}{}{} vale {}{}{}'.format(cores['amarelo'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa'], cores['verde'], s, cores['limpa']))
