altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }
area = largura * altura

litros = area / 2

print('A área da parede é de {}{}{} m² \nLogo, serão necessários {}{}{} litros de tinta'.format(cores['pretoebranco'], area, cores['limpa'], cores['pretoebranco'], litros, cores['limpa']))
