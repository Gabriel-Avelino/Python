import json


def cadastrar():

    while True:
        name = str(input('Nome: ')).strip().title()
        if name == '':
            print('\033[31mERRO: digite um nome válido.\033[m')
        else:
            break

    while True:
        try:
            age = int(input('Idade: '))
            adicionar(name, age)
            break
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0


def adicionar(nome, idade):
    try:
        with open("cadastro.txt", "a") as arquivo:
            cadastro = {
                'nome': nome,
                'idade': idade
            }
            json.dump(cadastro, arquivo)
            arquivo.write('\n')
        print(f'Novo registro de {nome} adicionado.')
    except:
        print('ERRO: ocorreu um erro inesperado.')


def ler():
    try:
        with open("cadastro.txt", "r") as arquivo:
            lista = []
            for l in arquivo:
                cadastro = json.loads(l)
                lista.append(cadastro)
            return lista
    except:
        print('ERRO: ocorreu um erro inesperado.')
