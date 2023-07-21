from utilidadesCeV.moeda.formatacao import moeda
from utilidadesCeV.moeda.calculos import dobro, aumentar, diminuir, metade


def resumo(value=0, aum=10, dim=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço Analisado:":<20}{moeda(value)}')
    print(f'{"Dobro do Preço:":<20}{dobro(value, True)}')
    print(f'{"Metade do Preço:":<20}{metade(value, True)}')
    print(f'{f"{aum}% de aumento:":<20}{aumentar(value, aum, True)}')
    print(f'{f"{dim}% de redução:":<20}{diminuir(value, dim, True)}')
    print('-' * 30)