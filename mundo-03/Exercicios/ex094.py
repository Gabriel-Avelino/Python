pessoas = []
ficha = dict()
total = 0

while True:
    ficha['nome'] = str(input('Nome: ')).strip().title()

    sexo = ''
    while sexo not in ['M', 'F']:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo not in ['M', 'F']:
            print('ERRO! Por favor, digite apenas M ou F.')
    ficha['sexo'] = sexo

    idade = 0
    while idade <= 0:
        idade = int(input('Idade: '))
        if idade <= 0:
            print('ERRO! Por favor, digite uma idade válida.')
    ficha['idade'] = idade
    total += ficha['idade']

    pessoas.append(ficha.copy())
    ficha.clear()

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar not in ['S', 'N']:
            print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-=' * 30)
media = total / len(pessoas)
print(f'''A) Ao todo temos {len(pessoas)} cadastradas.
B) A média de idade é de {media:5.2f} anos.
C) As mulheres cadastradas foram''', end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print(f'\nD) Lista de pessoas que estão acima da média:')
for h in pessoas:
    if h['idade'] >= media:
        print('     ', end='')
        for k, v in h.items():
            print(f'{k} = {v};', end=' ')
        print()
print("<< ENCERRADO >>")
