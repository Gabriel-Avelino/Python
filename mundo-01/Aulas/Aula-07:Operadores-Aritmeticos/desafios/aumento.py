salario = float(input('Digite o salário atual: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }
salario = salario + (salario * (15/100))

print('Seu novo salário será de: {}{}{}'.format(cores['verde'], salario, cores['limpa']))
