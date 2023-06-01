num = int(input('Digite um número inteiro: '))
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

conversao = str(input('''\033[36mEscolha a base numérica para a conversão:\033[m
\033[37m[1]\033[33m Binário
\033[37m[2]\033[33m Octal
\033[37m[3]\033[33m Hexadecimal\033[m
''')).title()

if conversao == '1' or conversao == 'Binário':
    print('{1}Binário: {2}{0}{3}'.format(bin(num).replace('0b', ''), cores['violeta'], cores['vermelho'], cores['limpa']))
elif conversao == '2' or conversao == 'Octal':
    print('{1}Octal: {2}{0}{3}'.format(oct(num).replace('0o', ''), cores['violeta'], cores['vermelho'], cores['limpa']))
elif conversao == '3' or conversao == 'Hexadecimal':
    print('{1}Hexadecimal: {2}{0}{3}'.format(hex(num).replace('0x', ''), cores['violeta'], cores['vermelho'], cores['limpa']))
else:
    print('\033[31mOpção inválida')
