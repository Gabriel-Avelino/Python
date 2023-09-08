while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 50)

    if tab < 0:
        break

    for c in range(1, 11):
        result = tab * c
        print(f'{tab} x {c} = {result}')
    print('-' * 50)
<<<<<<< HEAD
print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')
=======
print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')
>>>>>>> 76e9541fc56ed80fa6c5cd7fb328822de90d9965
