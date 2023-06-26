distancia = float(input('Digite a distância da sua viagem em km: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

if distancia <= 200:
    print('{1}O valor total da viagem será {2}R${0:.2f}{3}'.format(distancia * 0.5, cores['ciano'], cores['amarelo'], cores['limpa']))
else:
    print('{1}O valor total da viagem será {2}R${0:.2f}{3}'.format(distancia * 0.45, cores['ciano'], cores['amarelo'], cores['limpa']))
