pessoas = []
dados = []
maior = 0
menor = 0

while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))

    if not pessoas:
        menor = maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 35)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
