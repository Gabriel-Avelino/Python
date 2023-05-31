num = int(input('Digite um número inteiro entre 0 e 9999: '))
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

print('''{5}O número digitado foi {7}{0}{11}
{6}Unidade: {8}{1}{11}
{6}Dezena: {9}{2}{11}
{6}Centena: {10}{3}{11}
{6}Milhar {5}{4}{11}'''.format(num, num//1 % 10, num//10 % 10, num//100 % 10, num//1000 % 10, cores['amarelo'], cores['ciano'], cores['vermelho'], cores['violeta'], cores['verde'], cores['cinza'], cores['limpa']))
