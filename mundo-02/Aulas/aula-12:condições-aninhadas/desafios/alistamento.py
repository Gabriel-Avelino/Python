from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
atraso = idade - 18

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

if idade < 18:
    print('''{2}Você tem {0} anos: 
{3}Ainda não possui idade para se alistar.
Ainda faltam {1} ano(s) para o alistamento.{4}'''.format(idade, str(atraso).replace('-', ''), cores['ciano'], cores['verde'], cores['limpa']))
elif idade == 18:
    print('''{1}Você tem {0} anos: 
{2}Está na hora de se alistar.{3}'''.format(idade, cores['ciano'], cores['amarelo'], cores['limpa']))
elif idade > 18:
    print('''{2}Você tem {0} anos: 
{3}Se não tiver feito o alistamento, já passou da hora de se alistar.
Você se atrasou em {1} ano(s) para o alistamento.{4}'''.format(idade, atraso, cores['ciano'], cores['vermelho'], cores['limpa']))
