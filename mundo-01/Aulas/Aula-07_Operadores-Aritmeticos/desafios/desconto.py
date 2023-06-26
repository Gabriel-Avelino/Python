preco = float(input('Digite o preço do produto: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

preco = preco - (preco * (5/100))

print('O valor final da compra é de: R${:.2f}'.format(cores['ciano'], preco, cores['limpa']))
