some = input('Digite algo: ')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

print('Tipo: {}{}{}'.format(cores['vermelho'], type(some), cores['limpa']))
print('É alfanumérico?: {}{}{}'.format(cores['amarelo'], some.isalnum(), cores['limpa']))
print('São letras: {}{}{}'.format(cores['azul'], some.isalpha(), cores['limpa']))
print('É um código ASCII: {}{}{}'.format(cores['violeta'], some.isascii(), cores['limpa']))
print('É um número decimal: {}{}{}'.format(cores['ciano'], some.isdecimal(), cores['limpa']))
print('É um dígito: {}{}{}'.format(cores['pretoebranco'], some.isdigit(), cores['limpa']))
print('É um identificador: {}{}{}'.format(cores['verde'], some.isidentifier(), cores['limpa']))
print('São letras minúsculas: {}{}{}'.format(cores['vermelho'], some.islower(), cores['limpa']))
print('São números: {}{}{}'.format(cores['amarelo'], some.isnumeric(), cores['limpa']))
print('Pode ser impresso: {}{}{}'.format(cores['azul'], some.isprintable(), cores['limpa']))
print('São espaços: {}{}{}'.format(cores['violeta'], some.isspace(), cores['limpa']))
print('É um título: {}{}{}'.format(cores['ciano'], some.istitle(), cores['limpa']))
# Possui uma letra maiúscula no início e o restante das letras são minúsculas
print('São letras maiúsculas: {}{}{}'.format(cores['pretoebranco'], some.isupper(), cores['limpa']))
