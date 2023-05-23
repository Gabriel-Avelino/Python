preco = float(input('Digite o preço do produto: '))

preco = preco - (preco * (5/100))

print('O valor final da compra é de: R${:.2f}'.format(preco))
