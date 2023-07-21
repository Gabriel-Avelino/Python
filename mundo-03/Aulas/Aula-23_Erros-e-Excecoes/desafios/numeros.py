def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')


inteiro = leiaint('Digite um Inteiro: ')
real = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
