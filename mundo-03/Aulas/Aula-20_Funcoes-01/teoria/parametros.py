# Também é possível trabalhar com parâmetros nas funções:

def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem(f'{"Sistema de alunos":^30}')
mensagem(f'{"Cadastro de Funcionários":^30}')
mensagem(f'{"Erro de Sistema":^30}')
