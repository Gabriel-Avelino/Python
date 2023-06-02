a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro segmento: '))
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
if b - c < a < b + c and c - a < b < c + a and b - a < c < b + a:
    if a == b == c:
        tipo = 'Equilátero'
    elif a == b != c or a != b == c:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'

    print('{4}Os segmentos {5}{0}{4}, {5}{1}{4} e {5}{2}{4} formam um triângulo {6}{3}{7}.'.format(a, b, c, tipo, cores['ciano'], cores['cinza'], cores['verde'], cores['limpa']))
else:
    print('{3}Os segmentos {4}{0}{3}, {4}{1}{3} e {4}{2}{3} {5}NÃO{3} formam um triângulo{6}.'.format(a, b, c, cores['ciano'], cores['cinza'], cores['vermelho'], cores['limpa']))
