print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

cedulas = [50, 20, 10, 1]
c = 0

saque = int(input('Que valor você quer sacar? R$'))

while True:
    quantidade = saque // cedulas[c]
    resto = saque % cedulas[c]
    saque = resto
    if quantidade > 0:
        print(f'''Total de {quantidade} cédulas de R${cedulas[c]}''')
    c += 1
    if c >= 4:
        break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
