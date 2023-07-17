from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    if inicio < fim:
        fim += 1
    elif inicio > fim:
        fim -= 1
        if passo > 0:
            passo = -passo
    for c in range(inicio, fim, passo):
        sleep(.5)
        print(c, end=' ')
    sleep(.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
