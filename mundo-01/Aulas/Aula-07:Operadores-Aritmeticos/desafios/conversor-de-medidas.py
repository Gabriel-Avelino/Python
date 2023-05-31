metro = float(input('Digite a medida em metros: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }
centimetro = metro * 100
milimetro = metro * 1000

print('Valor em centímetros: {}{:.3f}{} cm \nValor em milímetros: {}{:.3f}{} mm'.format(cores['violeta'], centimetro, cores['limpa'], cores['amarelo'], milimetro, cores['limpa']))
