from datetime import date


def voto(nascimento):
    """
    -> Mostra se a pessoa possui direito ao voto ou não e se ele é obrigatório.
    :param nascimento: Data de nascimento usada para calcular a idade.
    :return: idade, status
    """

    idade = date.today().year - nascimento
    status = ''
    if idade < 16:
        status = 'NÃO VOTA'
    elif idade < 18 or idade >= 65:
        status = 'VOTO OPCIONAL'
    elif 18 <= idade < 65:
        status = 'VOTO OBRIGATÓRIO'

    return idade, status


print('-' * 30)
n = int(input('Em que ano você nasceu? '))
print(f'Com {voto(n)[0]} anos: {voto(n)[1]}')
