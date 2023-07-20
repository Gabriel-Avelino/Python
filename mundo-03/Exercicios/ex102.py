def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Recebe o número que terá o fatorial calculado.
    :param show: Parâmetro que definirá se os cálculos serão exibidos.
    :return: f (resultado do fatorial)
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} x' if c > 1 else f'{c} =', end=' ')
        f *= c
    return f


print('-' * 30)
print(fatorial(5, show=True))
help(fatorial)
