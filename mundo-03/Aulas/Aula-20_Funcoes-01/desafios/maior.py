from time import sleep


def maior(*nums):
    maiorvalor = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for c, v in enumerate(nums):
        print(v, end=' ')
        sleep(.5)
        if c == 0:
            maiorvalor = v
        else:
            if v > maiorvalor:
                maiorvalor = v
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {maiorvalor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
