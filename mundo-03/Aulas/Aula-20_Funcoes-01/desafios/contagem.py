from time import sleep


def contador(ini, end, count):
    if count == 0:
        count = 1

    print('-=' * 20)
    print(f'Contagem de {ini} até {end} de {abs(count)} em {abs(count)}')

    if ini > end:
        if count > 0:
            count = -count
        end -= 1
    elif ini < end:
        end += 1

    for c in range(ini, end, count):
        sleep(0.5)
        print(c, end=' ')
    sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
