money = float(input('Digite quanto dinheiro você tem: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

dolar = money / 3.27

print('Você pode comprar {}US${:.2f}{}'.format(cores['verde'], dolar, cores['limpa']))
