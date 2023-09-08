preco = float(input('Qual é o preço do produto?: R$'))
desconto = float(input('Qual o valor do desconto?: '))

print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}'.format(preco, desconto, (preco - (preco * desconto/100))))
