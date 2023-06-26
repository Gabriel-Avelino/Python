velocidade = float(input('Digite a velocidade do carro: '))
ultrapassado = velocidade - 80
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }
if velocidade > 80:
    print('{3}Você está a {4}{0}km/h{3}. \nUltrapassou o limite de velocidade em {4}{1}{3} km/h \ne será multado em {4}R${2:.2f}{5}'.format(velocidade, ultrapassado, ultrapassado * 7, cores['vermelho'], cores['amarelo'], cores['limpa']))
else:
    print('{1}Você está a {2}{0} km/h{1}. \nEstá dentro do limite de velocidade.{3}'.format(velocidade, cores['verde'], cores['amarelo'], cores['limpa']))
