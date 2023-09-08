from utilidadesCeV.moeda.formatacao import moeda


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