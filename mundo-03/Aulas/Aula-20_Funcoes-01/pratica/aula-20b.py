def contador(*num):
    print('Recebi os valores: ', end='')
    for valor in num:
        print(f'{valor} ', end='')
    print(f'\nSão ao todo {len(num)} números')
    print()


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
