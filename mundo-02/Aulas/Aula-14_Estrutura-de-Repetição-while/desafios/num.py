num = 0
c = 1
soma = 0
media = 0
maior = 0
menor = 0
continuar = ''

while continuar != 'N':
    num = int(input('Digite um número: '))
    soma += num
    media = soma / c
    c += 1

    if num > maior:
        maior = num
<<<<<<< HEAD
    if menor == 0:
=======
    if c == 1:
>>>>>>> 76e9541fc56ed80fa6c5cd7fb328822de90d9965
        menor = num
    elif num < menor:
        menor = num

    while continuar not in ['S', 's', 'N', 'n']:
        continuar = str(input('Deseja continuar? [S / N]: ')).upper().strip()
        if continuar not in 'SsNn':
            print('Digite uma opção válida.')
    if continuar == 'S' or continuar == 'SIM':
        continuar = 'S'
    elif continuar == 'N' or continuar == 'NÃO':
        continuar = 'N'
    if continuar == 'S':
        continuar = ''
print('''Média= {:.3f}
Maior = {}
Menor = {}'''.format(media, maior, menor))
