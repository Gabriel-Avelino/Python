casa = float(input('Digite o valor da compra: '))
salario = float(input('Digite o valor do seu salário: '))
anos = float(input('Em quantos anos deseja quitar a compra?: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

prestacao = casa / (anos * 12)

if prestacao > salario * 30/100:
    print('''{4}Sua compra tem o valor de {5}R${0:.2f}{4} e será quitada em {5}{1} anos{4}.
Sua parcela será de {5}R${2:.2f}{4} e seu salário é de {5}R${3:.2f}{4}. 
Logo, seu empréstimo foi {6}NEGADO{7}'''.format(casa, anos, prestacao, salario, cores['ciano'], cores['amarelo'], cores['vermelho'], cores['limpa']))
else:
    print('''{4}Sua compra tem o valor de {5}R${0:.2f}{4} e será quitada em {5}{1} anos{4}.
Sua parcela será de {5}R${2:.2f}{4} e seu salário é de {5}R${3:.2f}{4}. 
Logo, seu empréstimo foi {6}APROVADO{7}'''.format(casa, anos, prestacao, salario, cores['ciano'], cores['amarelo'], cores['verde'], cores['limpa']))
