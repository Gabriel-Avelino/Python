from random import randint
from unidecode import unidecode

print('=-' * 20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=-' * 20)
v = 0
opcao = ''

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)

    while opcao not in ['P', 'I']:
        opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        if opcao not in ['P', 'I']:
            print('Digite uma opção válida')

    soma = jogador + computador

    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'

    print('-' * 40)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {result}')
    print('-' * 40)

    if unidecode(result)[0] == opcao:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        v += 1
        print('=-' * 20)
    else:
        print('Você PERDEU!')
        print('=-' * 20)
        break
    opcao = ''
print(f'GAME OVER! Você venceu {v} vezes')
