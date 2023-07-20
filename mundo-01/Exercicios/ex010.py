money = float(input('Quanto dinheiro você tem na carteira?: R$'))

print('Com R${0:.2f}, você pode comprar US${1:.2f} \nCom R${0:.2f}, você pode comprar €{2:.2f} \nCom R${0:.2f}, você pode comprar £{3:.2f}'.format(money, money / 4.97, money/5.35, money / 6.16))
