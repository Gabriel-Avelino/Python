from calculos.formatacao import formatar
from calculos.moeda import *


def resumo(value, au, dim):

    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço Analisado:":<20}{formatar(value)}')
    print(f'{"Dobro do Preço:":<20}{dobro(value, True)}')
    print(f'{"Metade do Preço:":<20}{metade(value, True)}')
    print(f'{f"{au} de aumento:":<20}{aumentar(value, au, True)}')
    print(f'{f"{dim}% de redução:":<20}{diminuir(value, dim, True)}')
    print('-' * 30)
