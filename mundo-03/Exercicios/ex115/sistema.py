from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resp[0] == 1:
        # Listagem de conteúdo.
        lerarquivo(arq)
    elif resp[0] == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp[0] == resp[1]:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
