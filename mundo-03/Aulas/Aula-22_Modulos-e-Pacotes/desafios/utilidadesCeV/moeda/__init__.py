def moeda(v):
    v = f'R${v:.2f}'
    return v


def metade(value, form=False):
    if form:
        return moeda(value/2)
    else:
        return value / 2


def dobro(value, form=False):
    if form:
        return moeda(value * 2)
    else:
        return value * 2


def aumentar(value, por, form=False):
    value += (por/100) * value
    if form:
        return moeda(value)
    else:
        return value


def diminuir(value, por, form=False):
    value -= (por/100) * value
    if form:
        return moeda(value)
    else:
        return value


def resumo(value, au, dim):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço Analisado:":<20}{moeda(value)}')
    print(f'{"Dobro do Preço:":<20}{dobro(value, True)}')
    print(f'{"Metade do Preço:":<20}{metade(value, True)}')
    print(f'{f"{au} de aumento:":<20}{aumentar(value, au, True)}')
    print(f'{f"{dim}% de redução:":<20}{diminuir(value, dim, True)}')
    print('-' * 30)
