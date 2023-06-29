boletins = []
aluno = []
notas = []

while True:
    aluno.append(str(input('Nome: ')))
    for c in range(0, 2):
        notas.append(float(input(f'Nota {c + 1}: ')))
    aluno.append(notas[:])
    soma = 0

    for n in notas:
        soma += n
    media = soma / len(notas)
    aluno.append(media)
    boletins.append(aluno[:])
    notas.clear()
    aluno.clear()

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for c, b in enumerate(boletins):
    print(f'{c}  {b[0]} {b[2]:>10}')
