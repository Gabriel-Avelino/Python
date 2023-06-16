from random import randint
from random import choice
from time import sleep
proximo = ['JOGADOR', 'COMPUTADOR']
escolha = ['PAR', 'ÍMPAR']
jogadorEscolha = ''
computEscolha = ''
computNum = 0
jogadorNum = 0
soma = 0
c = 0

while True:
    vez = choice(proximo)
    if vez == 'JOGADOR':

        while True:
            jogadorEscolha = str(input('''Par ou ímpar?:
    [ 1 ] PAR
    [ 2 ] ÍMPAR
Sua escolha: ''')).upper().strip()[0]
            if jogadorEscolha == 'P' or jogadorEscolha == '1':
                jogadorEscolha = 'PAR'
                break
            elif jogadorEscolha == 'Í' or jogadorEscolha == '2' or jogadorEscolha == 'I':
                jogadorEscolha = 'ÍMPAR'
                break
            else:
                print('Selecione uma opção válida')

        if jogadorEscolha == 'PAR':
            computEscolha = 'ÍMPAR'
        else:
            computEscolha = 'PAR'
    else:
        computEscolha = choice(escolha)
        if computEscolha == 'ÍMPAR':
            jogadorEscolha = 'PAR'
        else:
            jogadorEscolha = 'ÍMPAR'
    print(f'Computador: "{computEscolha}"')
    sleep(1)
    print(f'Jogador: "{jogadorEscolha}"')

    computNum = randint(0, 10)
    jogadorNum = int(input('Digite um número de 1 a 10: '))

    soma = computNum + jogadorNum

    if soma % 2 == 0 and jogadorEscolha == 'PAR':
        print(f'''Eu escolhi {computNum}
Você escolheu {jogadorNum}
A soma deu {soma}
PARABÉNS! VOCÊ VENCEU!''')
        c += 1

    elif soma % 2 != 0 and jogadorEscolha == 'ÍMPAR':
        print(f'''Eu escolhi {computNum}
Você escolheu {jogadorNum}
A soma deu {soma}
PARABÉNS! VOCÊ VENCEU!''')
        c += 1

    else:
        print(f'''Eu escolhi {computNum}
Você escolheu {jogadorNum}
A soma deu {soma}
EU VENCI!''')
        break
print(f'Você venceu {c} rodadas seguidas')


