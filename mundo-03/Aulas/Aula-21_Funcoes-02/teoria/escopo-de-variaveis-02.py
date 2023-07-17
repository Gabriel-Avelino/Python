# Ao tentar alterar uma variável global diretamente no escopo local não alteramos ela.
# Na verdade criamos uma variável local de mesmo nome. Para alterar o valor global, precisamos fazer o seguinte:
def teste(b):
    # global a
    a = 8
    b += 4
    c = 2
    print(f'Na função teste, a vale {a}')
    print(f'Na função teste, b vale {b}')
    print(f'Na função teste, c vale {c}')


# Programa principal:
a = 5
teste(a)
print(f'A variável a do lado de fora vale {a}')

