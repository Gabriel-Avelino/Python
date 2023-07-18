def ficha(name, gols=0):
    """
    -> Recebe um nome e a quantidade de gols. Retorna uma mensagem com o nome e a quantidade.
    Se os dados não forem preenchidos, o nome retorna como desconhecido e a quantidade de gols retorna 0.
    :param name: Nome do jogador
    :param gols: Quantidade de Gols
    :return: name, gols
    """
    if name == '':
        name = '<desconhecido>'
    if gols == '':
        gols = 0
    return name, gols


print()
print('-' * 30)
nome_jogador = input('Nome do Jogador: ').strip().title()
num_gols = input('Número de Gols: ')

if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0

print(f'O jogador {ficha(nome_jogador, num_gols)[0]} fez {ficha(nome_jogador, num_gols)[1]} gol(s) no campeonato.')
