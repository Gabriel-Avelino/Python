def leiaint(mensagem):
    """
    -> Pede um input de um número inteiro para o usuário e retorna uma mensagem de erro caso não seja inteiro.
    Se for inteiro apenas retorna o valor.
    :param mensagem: Mensagem que será passada para o usuário digitar
    :return: num
    """
    while True:
        num = input(mensagem)
        if num.isnumeric():
            return num
        else:
            print(f'\033[031mERRO! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
