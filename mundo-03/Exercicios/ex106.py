from time import sleep

cores = ('\033[44m',  # Azul
         '\033[42m',  # Verde
         '\033[41m',  # Vermelho
         '\033[7;97m',  # Branco
         '\033[m')  # Default


def title(cor, t):
    tamanho = len(t) + 4
    print(f'{cores[cor]}{"~" * tamanho}')
    print(f'  {t}')
    print('~' * tamanho)
    print(cores[4], end='')
    sleep(1)


def dicionario(command):
    title(0, f'Acessando o manual do comando \'{command}\'')
    print(cores[3], end='')
    help(command)
    print(cores[4], end='')
    sleep(2)


while True:
    title(1, 'SISTEMA DE AJUDA PyHELP')
    c = str(input('Função ou Biblioteca > ')).strip().lower()
    if c == 'fim':
        break
    dicionario(c)

title(2, 'ATÉ LOGO!')
