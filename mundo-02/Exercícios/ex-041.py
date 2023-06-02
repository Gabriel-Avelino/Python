from datetime import date
ano = int(input('\033[33mAno de Nascimento: '))
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

idade = date.today().year - ano

if idade <= 9:
    classificacao = '\033[95mMIRIM'
elif idade <= 14:
    classificacao = '\033[94mINFANTIL'
elif idade <= 19:
    classificacao = '\033[92mJUNIOR'
elif idade <= 25:
    classificacao = '\033[93mSÊNIOR'
else:
    classificacao = '\033[91mMASTER'

input('''{2}O atleta tem {3}{0}{2} anos.
{4}Classificação: {1}'''.format(idade, classificacao, cores['cinza'], cores['ciano'], cores['limpa']))