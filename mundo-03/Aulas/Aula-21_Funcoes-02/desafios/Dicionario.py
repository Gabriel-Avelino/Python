def title(cor, titulo):
    tamanho = len(titulo) + 4
    print(f'{cor}{"~" * tamanho}')
    print(titulo.center(tamanho))
    print(f'{"~" * tamanho}')
    print('\033[m', end='')


def dicionario(comando):
    title('\033[44m', f'Acessando o manual do comando "{comando}"')
    print('\033[7;30;97m', end='')
    help(comando)
    print('\033[m', end='')


while True:
    title('\033[42m', 'SISTEMA DE AJUDA PyHELP')
    command = str(input('Função ou Biblioteca> ')).strip().lower()
    if command == 'fim':
        break
    dicionario(command)

title('\033[41m', 'ATÉ LOGO!')
