from random import randint
computador = randint(0, 10)
jogador = ''
dica = ''
tentativas = 1
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

while jogador != computador:
    jogador = int(input('Qual é seu palpite? '))
    if jogador != computador:
        if jogador < computador:
            dica = 'Mais'
            tentativas += 1
        elif jogador > computador:
            dica = 'Menos'
            tentativas += 1
        print('{}... Tente mais uma vez.'.format(dica))
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
