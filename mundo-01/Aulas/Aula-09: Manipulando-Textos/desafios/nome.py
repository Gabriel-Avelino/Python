nome = input('Digite seu nome completo: ').strip()
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:97m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

print('''{5}Nome: {6}{0}{11} 
{5}Nome em letras maiúsculas: {7}{1}{11} 
{5}Nome em letras minúsculas: {8}{2}{11} 
{5}Quantidade de letras: {9}{3}{11} 
{5}Quantidade de letras do primeiro nome: {10}{4}{11}'''.format(nome, nome.upper(), nome.lower(), len(nome.replace(' ', '')), len(nome.split()[0]), cores['amarelo'], cores['vermelho'], cores['azul'], cores['violeta'], cores['ciano'], cores['verde'], cores['limpa']))
