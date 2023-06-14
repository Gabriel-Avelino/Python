from random import randint

jogador = 0
tentativas = 1
aleatorio = randint(0, 10)
print('-=-' * 30, '\nVou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 30)


while jogador != aleatorio:
    jogador = int(input('Digite um número de 1 a 10: '))

    if jogador == aleatorio:
        print('PARABÉNS! Você acertou o número!')
    else:
        print('Não foi nesse número que eu pensei...')
        tentativas += 1
print('Você precisou de {} tentativa(s)'.format(tentativas))
print('FIM DE JOGO')