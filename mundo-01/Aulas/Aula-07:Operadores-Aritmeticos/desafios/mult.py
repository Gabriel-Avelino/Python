num = int(input('Digite um número: '))
double = num * 2
triple = num * 3
raiz = num ** (1/2)
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

print('O dobro de {4}{0}{5} é: {6}{1}{5} \nO triplo de {4}{0}{5} é: {6}{2}{5} \nA raiz quadrada de {4}{0}{5} é: {6}{3}{5}'.format(num, double, triple, raiz, cores['amarelo'], cores['limpa'], cores['verde']))
