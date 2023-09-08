valores = []
pares = []
impares = []

while True:
    numero = int(input('Digite um valor: '))

    valores.append(numero)

    while True:
        continuar = ''
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in ['N', 'S']:
            break
    if continuar == 'N':
        break

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'''A lista completa é {valores}
A lista de pares é {pares}
A lista de ímpares é {impares}''')
