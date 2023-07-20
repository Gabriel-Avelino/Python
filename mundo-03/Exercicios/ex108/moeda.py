def dobro(value=0):
    return value * 2


def metade(value=0):
    return value / 2


def aumentar(value=0, por=0):
    value += (por / 100) * value
    return value


def diminuir(value=0, por=0):
    value -= (por / 100) * value
    return value


def formatar(value=0, moeda='R$'):
    return f'{moeda}{value:.2f}'.replace('.', ',')
