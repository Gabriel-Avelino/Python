maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    elif menor == 0 or peso < menor:
        menor = peso
print('''O maior peso lido foi de {}Kg
O menor peso lido foi de {}Kg'''.format(maior, menor))
