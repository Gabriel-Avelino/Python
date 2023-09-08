# É possível definir parâmetros opcionais para uma função. Para fazer isso basta usar o seguinte método:
def soma(a=0, b=0, c=0):
    """
    -> Soma três valores e exibe o resultado na tela.

    :param a: o primeiro valor.
    :param b: o segundo valor.
    :param c: o terceiro valor.
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 5)
soma(8, 4)
soma()
