salario = float(input('Digite o salário do funcionário: R$'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

if salario > 1250:
    print('{2}Esse funcionário recebe {3}R${0:.2f}{2}. Logo, seu novo salário será de {4}R$ {1:.2f}{5}'.format(salario, (salario + (salario * (10 / 100))), cores['ciano'], cores['vermelho'], cores['verde'], cores['limpa']))
else:
    print('{2}Esse funcionário recebe {3}R${0:.2f}.{2} Logo, seu novo salário será de {4}R$ {1:.2f}{5}'.format(salario, (salario + (salario * (15 / 100))), cores['ciano'], cores['vermelho'], cores['verde'], cores['limpa']))
