nome = input('Digite seu nome completo: ').strip()
separado = nome.split()
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

print('{2}Primeiro nome: {3}{0}{5} \n{2}Último nome: {4}{1}{5}'.format(separado[0], separado[-1], cores['amarelo'], cores['ciano'], cores['violeta'], cores['limpa']))
