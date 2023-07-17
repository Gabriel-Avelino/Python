maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso
print("""O maior peso foi: {} kg
O menor peso foi: {} kg """.format(maior, menor))
