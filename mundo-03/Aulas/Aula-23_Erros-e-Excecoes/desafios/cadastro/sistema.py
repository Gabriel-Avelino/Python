from manipular import *
from formatar import *


while True:
    title('MENU PRINCIPAL')
    op = int(input(f'''\033[33m1-\033[34m Ver Pessoas Cadastradas
\033[33m2-\033[34m Cadastrar Nova Pessoa
\033[33m3-\033[34m Sair do Sistema\033[m
{"-" * 50}
Sua Opção: '''))
    if op == 1:
        try:
            texto = ler()
            table(texto)
        except:
            print(f'\033[31mERRO: nenhum cadastro encontrado.\033[m')
    elif op == 2:
        title('NOVO CADASTRO')
        cadastrar()
    elif op == 3:
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
