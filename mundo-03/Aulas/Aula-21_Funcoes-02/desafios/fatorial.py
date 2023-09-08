def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número recebendo dois parâmetros.
    :param n: Número cujo fatorial será calculado.
    :param show: Define se o cálculo será exibido ou não.
    :return: expressao, f
    """

    f = 1
    expressao = ''
    for v in range(n, 0, -1):
        if show:
            expressao += f' {v} x' if v > 1 else f' {v} = '
        f *= v
    return expressao, f


result = fatorial(5, True)
tamanho = len(str(result[1])) + len(result[0].strip()) + 8
print('-' * tamanho)
print(result[0].strip(), str(result[1]))
