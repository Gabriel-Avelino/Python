a = float(input('\033[35mPrimeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'azul-claro': '\033[96m',
         'verde-claro': '\033[92m'
         }

if a - b < c < a + b and a - c < b < a + c and b - c < a < b + c:
    if a == b == c:
        tipo = '\033[37mEQUILÁTERO'
    elif a != b != c != a:
        tipo = '\033[33mESCALENO'
    else:
        tipo = '\033[94mISÓSCELES'
    print('{1}Os segmentos acima {2}PODEM FORMAR{1} um triângulo {0}{1}!'.format(tipo, cores['ciano'], cores['verde']))
else:
    print('{0}Os segmentos acima {1}NÃO PODEM FORMAR{0} um triângulo'.format(cores['ciano'], cores['vermelho']))
