def leiaint(mensagem):
    while True:
        num = input(mensagem)
        if num.isnumeric():
            return num
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
