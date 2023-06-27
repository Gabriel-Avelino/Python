valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um número: ')))

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
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
