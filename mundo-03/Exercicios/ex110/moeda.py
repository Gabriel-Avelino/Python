def dobro(value=0, f=False):
    return moeda(value * 2) if f else value * 2


def metade(value=0, f=False):
    return moeda(value / 2) if f else value / 2


def aumentar(value=0, por=0, f=False):
    value += (por / 100) * value
    return moeda(value) if f else value


def diminuir(value=0, por=0, f=False):
    value -= (por / 100) * value
    return moeda(value) if f else value


def moeda(value=0.0, moeda='R$'):
    return f'{moeda}{value:.2f}'.replace('.', ',')


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
