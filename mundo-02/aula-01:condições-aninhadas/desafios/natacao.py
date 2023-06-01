from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
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
idade = date.today().year - ano

if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 20:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print('''{2}O(a) atleta tem {3}{0}{2} anos.
{4}Sua categoria é: {5}{1}{6}'''.format(idade, categoria, cores['violeta'], cores['azul'], cores['vermelho'], cores['amarelo'], cores['limpa']))
