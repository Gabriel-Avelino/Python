from calculos.formatacao import formatar


def metade(value, form=False):
    if form:
        return formatar(value / 2)
    else:
        return value / 2


def dobro(value, form=False):
    if form:
        return formatar(value * 2)
    else:
        return value * 2


def aumentar(value, por, form=False):
    value += (por/100) * value
    if form:
        return formatar(value)
    else:
        return value


def diminuir(value, por, form=False):
    value -= (por/100) * value
    if form:
        return formatar(value)
    else:
        return value
