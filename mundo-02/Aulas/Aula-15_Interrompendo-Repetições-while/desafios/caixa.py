notas = [50, 20, 10, 1]
c = 0

print('=' * 40)
print('{:^40}'.format('BANCO GA'))
print('=' * 40)

valor = int(input('Qual valor será sacado? R$'))

while True:
    quantidade = valor // notas[c]
    print(f'Total de {quantidade} cédulas de R${notas[c]}')
    resto = valor % notas[c]
    c += 1
    valor = resto
    if c == 4:
        break
print('=' * 40)
print('Volte sempre ao BANCO GA! Tenha um bom dia!')
