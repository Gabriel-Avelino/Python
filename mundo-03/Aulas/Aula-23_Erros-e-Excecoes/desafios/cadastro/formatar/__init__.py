def title(t):
    print('-' * 50)
    print(t.center(50))
    print('-' * 50)


def table(info):
    title('PESSOAS CADASTRADAS')
    for v in info:
        for c, valor in enumerate(v.values()):
            print(f'{str(valor):<35}' if c == 0 else f'{f"{str(valor)} anos"}', end=' ')
        print()
