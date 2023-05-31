ano = int(input('Digite o ano desejado: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'
         }

if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:
    print('{1}O ano {2}{0}{1} é bissexto{3}.'.format(ano, cores['verde'], cores['amarelo'], cores['limpa']))
else:
    print('{1}O ano {2}{0}{1} não é bissexto{3}.'.format(ano, cores['verde'], cores['amarelo'], cores['limpa']))
