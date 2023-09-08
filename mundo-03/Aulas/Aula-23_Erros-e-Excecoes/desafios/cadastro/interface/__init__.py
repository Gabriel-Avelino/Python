def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def menu(lista):
    for c, op in enumerate(lista):
        print(f'\033[33m{c + 1}- \033[34m{op}\033[m')
    print('-' * 50)
    opcao = leiaint('\033[32mSua Opção: \033[m')
    tam = len(lista)

    return opcao, tam
