from random import choice
from time import sleep
game = ['PEDRA', 'PAPEL', 'TESOURA']

jogador = str(input('''\033[36mSuas opções:
\033[34m[ 0 ] \033[33mPEDRA
\033[34m[ 1 ] \033[33mPAPEL
\033[34m[ 2 ] \033[33mTESOURA
\033[37mQual é a sua jogada? ''')).upper().strip()
computador = choice(game)

print('\033[33mJO')
sleep(1)
print('KEM')
sleep(1)
print('PO\033[m')

if jogador == '0' or jogador == 'PEDRA':
    jogador = 'PEDRA'
elif jogador == '1' or jogador == 'PAPEL':
    jogador = 'PAPEL'
elif jogador == '2' or jogador == 'TESOURA':
    jogador = 'TESOURA'

print('-=' * 11)
if jogador == 'PEDRA' or jogador == 'PAPEL' or jogador == 'TESOURA':
    print('''\033[35mComputador jogou {0}
Jogador jogou {1}\033[m'''.format(computador, jogador))
    print('-=' * 11)
    if jogador == computador:
        msg = '\033[37mEMPATE'
    elif jogador == 'PEDRA' and computador == 'TESOURA':
        msg = '\033[92mJOGADOR VENCE'
    elif jogador == 'PAPEL' and computador == 'PEDRA':
        msg = '\033[92mJOGADOR VENCE'
    elif jogador == 'TESOURA' and computador == 'PAPEL':
        msg = '\033[92mJOGADOR VENCE'
    else:
        msg = '\033[91mCOMPUTADOR VENCE'
    print(msg)
else:
    print('\033[31mSelecione uma opção válida.')
