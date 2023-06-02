from time import sleep
valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = float(input('Quantos anos de financiamento? '))

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

parcela = valor / (ano * 12)
if parcela > salario * 30 / 100:
    emprestimo = '\033[31mNEGADO\033[35m'
else:
    emprestimo = 'pode ser \033[32mCONCEDIDO\033[35m'
    print('{}ANALISANDO...'.format(cores['vermelho']))
    sleep(5)
print('{4}Para pagar uma casa de {5}R${0:.2f}{4} em {5}{1}{4} anos, \na prestação será de {5}R${2:.2f}{4}. \nEmpréstimo {3}!'.format(valor, ano, parcela, emprestimo, cores['violeta'], cores['amarelo']))
