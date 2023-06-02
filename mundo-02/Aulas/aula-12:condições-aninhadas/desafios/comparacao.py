primeiro = int(input('\033[31mDigite um número inteiro: '))
segundo = int(input('Digite outro número inteiro: '))

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

if primeiro > segundo:
    print('{3}O primeiro valor ({2}{0}{3}) é maior que o segundo valor ({2}{1}{3}){4}'.format(primeiro, segundo, cores['amarelo'], cores['ciano'], cores['limpa']))
elif primeiro < segundo:
    print('{3}O segundo valor ({2}{1}{3}) é maior que o primeiro valor ({2}{0}{3}){4}'.format(primeiro, segundo, cores['amarelo'], cores['ciano'], cores['limpa']))
else:
    print('{}Não existe valor maior, os dois valores são iguais{}'.format(cores['ciano'], cores['limpa']))
