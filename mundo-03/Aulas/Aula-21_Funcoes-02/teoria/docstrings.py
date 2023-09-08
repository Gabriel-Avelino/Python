# Docstrings são strings de documentação, onde estão armazenadas as infromações de funcionamento de comandos do Python.
# É possível criar uma docstring da seguinte forma:

def contador(i, f, p):
    """
    -> Faz uma contagem e exibe na tela. Ao final também exibe uma mensagem,
    indicando o fim da sequência.

    :param i: Início da sequência.
    :param f: Final da sequência.
    :param p: Razão da sequência.
    :return: Não possui retorno.
    """
    if p == 0:
        p = 1

    if i > f:
        if p > 0:
            p = -p
        f -= 1
    elif i < f:
        f += 1

    for c in range(i, f, p):
        print(c, end=' ')
    print('PRONTO!')


contador(10, 1, 0)
help(contador)
