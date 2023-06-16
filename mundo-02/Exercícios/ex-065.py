soma = 0
c = 0
maior = 0
menor = 0
opcao = ''

while opcao != 'N':
    num = float(input('Digite um número: '))
    soma += num
    c += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    while opcao not in ['S', 's', 'N', 'n']:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
        if opcao == 'SIM':
            opcao = 'S'
        if opcao == 'NÃO':
            opcao = 'N'
        if opcao not in 'SsNn':
            print('Digite uma opção válida')
    if opcao == 'S':
        opcao = ''
media = soma / c
print('''Você digitou  {} números e a média foi {:.2f}
O maior valor foi {} e o menor foi {}'''.format(c, media, maior, menor))