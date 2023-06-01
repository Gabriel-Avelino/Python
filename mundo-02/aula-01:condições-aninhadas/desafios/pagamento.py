preco = float(input('\033[36mDigite o preço do produto: R$'))
pagamento = str(input('''\033[33mSelecione a forma de pagamento:
\033[34m[1] \033[37mÀ vista no dinheiro/cheque
\033[34m[2] \033[37mÀ vista no cartão
\033[34m[3] \033[37mEm até 2x no cartão
\033[34m[4] \033[37mEm 3x ou mais no cartão
'''))
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

if pagamento == 'À vista no dinheiro/cheque' or pagamento == '1':
    pagamento = 'À vista no dinheiro/cheque'
    preco -= preco * 10/100
    print('''{2}A forma de pagamento escolhida foi: {3}{0}{2}. 
{4}O valor da compra será de: {5}R${1:.2f}{6}'''.format(pagamento, preco, cores['azul'], cores['verde'], cores['cinza'], cores['amarelo'], cores['limpa']))
elif pagamento == 'À vista no cartão' or pagamento == '2':
    pagamento = 'À vista no cartão'
    preco -= preco * 5 / 100
    print('''{2}A forma de pagamento escolhida foi: {3}{0}{2}. 
{4}O valor da compra será de: {5}R${1:.2f}{6}'''.format(pagamento, preco, cores['azul'], cores['verde'], cores['cinza'], cores['amarelo'], cores['limpa']))
elif pagamento == 'Em até 2x no cartão' or pagamento == '3':
    pagamento = 'Em até 2x no cartão'
    preco = preco
    print('''{2}A forma de pagamento escolhida foi: {3}{0}{2}. 
{4}O valor da compra será de: {5}R${1:.2f}{6}'''.format(pagamento, preco, cores['azul'], cores['verde'], cores['cinza'], cores['amarelo'], cores['limpa']))
elif pagamento == 'Em 3x ou mais no cartão' or pagamento == '4':
    pagamento = 'Em 3x ou mais no cartão'
    preco += preco * 20/100
    print('''{2}A forma de pagamento escolhida foi: {3}{0}{2}. 
{4}O valor da compra será de: {5}R${1:.2f}{6}'''.format(pagamento, preco, cores['azul'], cores['verde'], cores['cinza'], cores['amarelo'], cores['limpa']))
else:
    print('{}Opção inválida{}'.format(cores['vermelho'], cores['limpa']))

