from unicodedata import normalize
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:97m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

frase = input('Digite uma frase: ').strip()
normalizada = normalize('NFD', frase).encode('ascii', 'ignore').decode('ascii')

print(normalizada)

print('''{4}A frase digitada foi: {5}{0}{9}
{4}Quantas vezes aparece a letra A: {6}{1}{9}
{4}Em que posição ela aparece primeiro?: {7}{2}ª posição{9}
{4}Em que posição ela aparece pela última vez: {8}{3}ª posição{9}
'''.format(frase, normalizada.upper().count('A'), normalizada.upper().find('A') + 1, normalizada.upper().rfind('A') + 1, cores['ciano'], cores['violeta'], cores['amarelo'], cores['vermelho'], cores['verde'], cores['limpa']))
