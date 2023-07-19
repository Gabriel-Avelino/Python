from formatacao import moeda


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
