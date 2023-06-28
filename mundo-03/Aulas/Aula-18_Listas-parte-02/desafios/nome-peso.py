pessoas = []
dados = []
maiorPeso = 0
menorPeso = 0

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for c, p in enumerate(pessoas):
    if c == 1:
        maiorPeso = menorPeso = p[1]

    if p[1] > maiorPeso:
        maiorPeso = p[1]

    if p[1] < menorPeso:
        menorPeso = p[1]

print('-=' * 30)
print(f'''Ao todo você cadastrou {len(pessoas)} pessoas.
O maior peso foi de {maiorPeso}Kg. Peso de''', end=' ')
for p in pessoas:
    if p[1] == maiorPeso:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menorPeso}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menorPeso:
        print(p[0], end=' ')
