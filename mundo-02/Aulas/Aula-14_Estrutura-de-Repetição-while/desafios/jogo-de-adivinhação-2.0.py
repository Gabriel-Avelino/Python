from random import randint
<<<<<<< HEAD
=======

>>>>>>> 76e9541fc56ed80fa6c5cd7fb328822de90d9965
jogador = ''
tentativas = 1
aleatorio = randint(0, 10)
print('-=-' * 30, '\nVou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 30)

<<<<<<< HEAD

=======
>>>>>>> 76e9541fc56ed80fa6c5cd7fb328822de90d9965
while jogador != aleatorio:
    jogador = int(input('Digite um número de 0 a 10: '))

    if jogador == aleatorio:
        print('PARABÉNS! Você acertou o número!')
    else:
        print('Não foi nesse número que eu pensei...')
        tentativas += 1
print('Você precisou de {} tentativa(s)'.format(tentativas))
<<<<<<< HEAD
print('FIM DE JOGO')
=======
print('FIM DE JOGO')
>>>>>>> 76e9541fc56ed80fa6c5cd7fb328822de90d9965
