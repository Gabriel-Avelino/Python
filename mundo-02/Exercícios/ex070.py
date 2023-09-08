menorPreco = 0
produtoMaisBarato = ''
maisDeMil = 0
total = 0

print('-' * 40)
print('{:^40}'.format('LOJÃO BARATÃO'))
print('-' * 40)

while True:
    produto = str(input('Nome do Produto: ')).title().strip()
    preco = float(input('Preço: R$'))

    total += preco

    if preco > 1000:
        maisDeMil += 1

    if preco < menorPreco or menorPreco == 0:
        menorPreco = preco
        produtoMaisBarato = produto

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar not in ['S', 'N']:
            print('Digite uma opção válida: ')

    if continuar == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'''O total da compra foi R${total:.2f}
Temos {maisDeMil} produtos custando mais de R$1000.00
O produto mais barato foi {produtoMaisBarato} que custa R${menorPreco:.2f}''')
