num = int(input('Digite um número: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

vezes1 = num * 1
vezes2 = num * 2
vezes3 = num * 3
vezes4 = num * 4
vezes5 = num * 5
vezes6 = num * 6
vezes7 = num * 7
vezes8 = num * 8
vezes9 = num * 9
vezes10 = num * 10

print('{11}{0} x 1 ={12} {1} \n{11}{0} x 2 ={12} {2} \n{11}{0} x 3 ={12} {3} \n{11}{0} x 4 ={12} {4} \n{11}{0} x 5 ={12} {5} \n{11}{0} x 6 ={12} {6} \n{11}{0} x 7 ={12} {7} \n{11}{0} x 8 ={12} {8} \n{11}{0} x 9 ={12} {9} \n{11}{0} x 10 ={12} {10}'.format(num, vezes1, vezes2, vezes3, vezes4, vezes5, vezes6, vezes7, vezes8, vezes9, vezes10, cores['amarelo'], cores['verde']))
