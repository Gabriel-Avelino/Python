ficha = {}
pessoas = []
total = 0

while True:
    ficha['nome'] = str(input('Nome: ')).strip().title()
    ficha['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    ficha['idade'] = int(input('Idade: '))
    pessoas.append(ficha.copy())

    continuar = ''
    while continuar not in ['N', 'S']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 35)
print(f'- O grupo tem {len(pessoas)} pessoas.')

for p in pessoas:
    total += p['idade']
media = total/len(pessoas)
print(f'- A média de idade é de {media:.2f} anos')

print(f'- As mulheres cadastradas foram:', end=' ')
for m in pessoas:
    if m['sexo'] == 'F':
        print(m['nome'], end=' ')

print(f'\n- Lista de pessoas que estão acima da média:')
for i in pessoas:
    print()
    for k, v in i.items():
        if i['idade'] > media:
            print(f'{k} = {v};', end=' ')
print("<< ENCERRADO >>")
