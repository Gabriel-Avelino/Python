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
    if c == 1:
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
