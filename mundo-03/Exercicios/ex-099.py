from time import sleep


def maior(*nums):
    maior = 0
    print('-=' * 30)
    print('Analisando valores...')
    for c, v in enumerate(nums):
        print(v, end=' ')
        sleep(.5)
        if c == 0:
            maior = v
        else:
            if v > maior:
                maior = v
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
