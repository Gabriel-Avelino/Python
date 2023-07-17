# O escopo é o local onde uma variável existe ou não dentro de um programa:
def teste():
    x = 8  # Aqui x está no escopo local.
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal:
n = 2  # Aqui n está no escopo global.
print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}')  # Gera erro porque x só existe dentro da função.
teste()
