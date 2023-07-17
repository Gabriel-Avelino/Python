while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 50)

    if tab < 0:
        break

    for c in range(1, 11):
        result = tab * c
        print(f'{tab} x {c} = {result}')
    print('-' * 50)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')
