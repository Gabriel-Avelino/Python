a = int(input('\033[36mPrimeiro número: '))
b = int(input('Segundo número: '))
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

if a != b:
    if a > b:
        comparacao = 'PRIMEIRO'
        corescolhida = cores['verde']
    elif a < b:
        comparacao = 'SEGUNDO'
        corescolhida = cores['vermelho']
    print('{1}O {0} valor é maior'.format(comparacao, corescolhida))
else:
    print('{}Os dois valores são IGUAIS.'.format(cores['amarelo']))
