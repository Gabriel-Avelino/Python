from time import sleep
from random import randint
numeros = []


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
def sorteio():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for v in numeros:
        print(v, end=' ')
        sleep(.5)
    print('PRONTO!')


def somapar(lista):
    total = 0
    for n in lista:
        if n % 2 == 0:
            total += n
    print(f'Somando os valores pares de {lista}, temos {total}')


sorteia(numeros)
somapar(numeros)

def somapar():
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += n
    print(f'Somando os valores pares de {numeros}, temos {total}')


sorteio()
somapar()

