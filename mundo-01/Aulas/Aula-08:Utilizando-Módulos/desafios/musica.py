import os
os.chdir("musicas-desafio21")
file = input("\033[34mDigite a música que você deseja tocar: \033[m")
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

print('Tocando "{1}{0}{2}" usando player nativo'.format(file, cores['amarelo'], cores['limpa']))
os.system("afplay " + file)
