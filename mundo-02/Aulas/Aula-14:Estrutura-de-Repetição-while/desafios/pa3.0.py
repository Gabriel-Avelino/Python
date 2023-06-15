from time import sleep

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termos = 11
novosTermos = termos
c = 1

while novosTermos != 0:
    while c < termos:
        result = primeiro + (c - 1) * razao
        print(result, end=' → ')
        c += 1
    print('...')
    novosTermos = int(input('\nDigite a quantidade de termos que você deseja ver: '))
    if novosTermos != 0:
        termos += novosTermos
        while c < termos:
            result = primeiro + (c - 1) * razao
            print(result, end=' → ')
            c += 1
    else:
        novosTermos = 0
print('FINALIZANDO PROGRAMA')
sleep(2)
print('\nPROGRAMA FINALIZADO')
