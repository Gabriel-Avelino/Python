from random import randint
from time import sleep

numeros = []


def sorteio():
    for c in range(0, 5):
        numeros.append(randint(1, 10))

    print('Sorteando 5 valores da lista: ', end='')
    for v in numeros:
        sleep(.5)
        print(v, end=' ')
    sleep(.5)
    print('PRONTO!')


def somapar(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    print(f'Somando os valores {lst}, temos {total}')


sorteio()
somapar(numeros)
