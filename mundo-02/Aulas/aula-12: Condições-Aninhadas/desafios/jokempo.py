from random import choice
jokempo = ['Pedra', 'Papel', 'Tesoura']
computador = choice(jokempo)
jogador = str(input('''\033[33mEscolha pedra, papel ou tesoura:
\033[34m[1] \033[37mPedra
\033[34m[2] \033[37mPapel
\033[34m[3] \033[37mTesoura
''')).title()
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

if computador == 'Pedra' and jogador == 'Pedra' or computador == 'Tesoura' and jogador == 'Tesoura' or computador == 'Papel' and jogador == 'Papel' or computador == 'Pedra' and jogador == '1' or computador == 'Tesoura' and jogador == '3' or computador == 'Papel' and jogador == '2':
    print('{1}Escolhi {2}{0}{1}! {3}EMPATE{1}!'.format(computador, cores['ciano'], cores['violeta'], cores['amarelo']))
elif computador == 'Pedra' and jogador == 'Tesoura' or computador == 'Tesoura' and jogador == 'Papel' or computador == 'Papel' and jogador == 'Pedra':
    print('{1}Escolhi {2}{0}{1}! {3}VENCI{1}!'.format(computador, cores['ciano'], cores['violeta'], cores['verde']))
elif computador == 'Papel' and jogador == 'Tesoura' or computador == 'Pedra' and jogador == 'Papel' or computador == 'Tesoura' and jogador == 'Pedra':
    print('{1}Escolhi {2}{0}{1}! {3}PERDI{1}!'.format(computador, cores['ciano'], cores['violeta'], cores['vermelho']))

elif computador == 'Pedra' and jogador == '3' or computador == 'Tesoura' and jogador == '2' or computador == 'Papel' and jogador == '1':
    print('{1}Escolhi {2}{0}{1}! {3}VENCI{1}!'.format(computador, cores['ciano'], cores['violeta'], cores['verde']))
elif computador == 'Papel' and jogador == '3' or computador == 'Pedra' and jogador == '2' or computador == 'Tesoura' and jogador == '1':
    print('{1}Escolhi {2}{0}{1}! {3}PERDI{1}!'.format(computador, cores['ciano'], cores['violeta'], cores['vermelho']))

