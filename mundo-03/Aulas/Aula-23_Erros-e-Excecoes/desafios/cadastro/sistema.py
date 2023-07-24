from manipular import *
from formatar import *
from interface import *
from time import sleep


while True:
    title('MENU PRINCIPAL')
    op = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if op[0] == 1:
        try:
            texto = ler()
            table(texto)
        except:
            print(f'\033[31mERRO: nenhum cadastro encontrado.\033[m')
    elif op[0] == 2:
        title('NOVO CADASTRO')
        cadastrar()
    elif op[0] == op[1]:
        title('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
