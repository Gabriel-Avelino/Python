from datetime import date
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

sexo = str(input('''\033[33mSexo: 
\033[37m[ 1 ] \033[34mMasculino
\033[37m[ 2 ] \033[35mFeminino
\033[37mSua Opção: ''')).title()
if sexo == 'Masculino' or sexo == '1':
    print('{}Você é do sexo MASCULINO. \nLogo, o alistamento é obrigatório para você, caso tenha 18 anos.'.format(cores['azul']))

    ano = int(input('\033[33mAno de Nascimento: '))
    atual = date.today().year
    idade = atual - ano
    diferenca = idade - 18
    alistamento = atual - diferenca

    print('{3}Quem nasceu em {4}{0}{3} tem {4}{1}{3} anos em {4}{2}'.format(ano, idade, atual, cores['violeta'],
                                                                            cores['azul']))
    if idade < 18:
        print('''{2}Ainda faltam {3}{0}{2} ano(s) para o alistamento.
Seu alistamento será em {3}{1}{2}.'''.format(abs(diferenca), alistamento, cores['verde'], cores['cinza']))
    elif idade > 18:
        print('''{2}Você já deveria ter se alistado há {3}{0}{2} ano(s).
Seu alistamento foi em {3}{1}{2}.'''.format(abs(diferenca), alistamento, cores['vermelho'], cores['cinza']))
    else:
        print('{0}Você deve se alistar IMEDIATAMENTE!'.format(cores['amarelo']))

elif sexo == 'Feminino' or sexo == '2':
    print('{}Você é do sexo FEMININO. \nLogo, o alistamento não é obrigatório para você.'.format(cores['violeta']))
else:
    print('{}Opção inválida'.format(cores['vermelho']))
