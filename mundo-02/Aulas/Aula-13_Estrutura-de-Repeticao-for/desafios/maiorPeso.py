maior = 0
menor = 0
<<<<<<< HEAD
for c in range(0,5):
=======
for c in range(0, 5):
>>>>>>> 76e9541fc56ed80fa6c5cd7fb328822de90d9965
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso
print("""O maior peso foi: {} kg
<<<<<<< HEAD
O menor peso foi: {} kg """.format(maior, menor))
=======
O menor peso foi: {} kg """.format(maior, menor))
>>>>>>> 76e9541fc56ed80fa6c5cd7fb328822de90d9965
