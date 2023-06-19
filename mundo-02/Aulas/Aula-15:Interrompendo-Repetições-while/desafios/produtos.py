total = 0
maisDeMil = 0
maisBarato = ''
menorPreco = 0
continuar = ''

print('-' * 30)
print('{:^30}'.format('Loja do Baratão'))
print('-' * 30)

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Informe o valor do produto: R$'))

    total += preco

    if preco > 1000:
        maisDeMil += 1

    if preco < menorPreco or menorPreco == 0:
        menorPreco = preco
        maisBarato = nome

    while continuar not in ['S', 'N']:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar not in ['S', 'N']:
            print('Digite uma opção válida')

    if continuar == 'N':
        break
    continuar = ''

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'''O total da compra foi R${total:.2f}
Temos {maisDeMil} produtos custando mais de R$ 1000.00
O produto mais barato foi {maisBarato} que custa R${menorPreco:.2f}''')
