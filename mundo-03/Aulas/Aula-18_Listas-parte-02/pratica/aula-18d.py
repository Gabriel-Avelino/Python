pessoas = list()
dados = list()
totalMaior = totalMenor = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()

print(pessoas)

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalMenor += 1

print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade.')
