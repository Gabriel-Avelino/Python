peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
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

imc = peso / altura ** 2

if imc < 18.5:
    status = '\033[34mAbaixo do Peso'
elif 18.5 <= imc < 25:
    status = '\033[32mPeso Ideal'
elif 25 <= imc < 30:
    status = '\033[33mSobrepeso'
elif 30 <= imc <= 40:
    status = '\033[31mObesidade'
elif imc > 40:
    status = '\033[37mObesidade Mórbida'

print('''{2}Seu IMC é {3}{0}{2}:
Você está: {1}{4}'''.format(imc, status, cores['ciano'], cores['amarelo'], cores['limpa']))
