boletins = []
aluno = []
notas = []

while True:
    aluno.append(str(input('Nome: ')).strip().title())

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

print('-=' * 30)
print(f'{"No.":<6}{"NOME":<10} {"MÉDIA":>10}')
print('-' * 30)
for c, b in enumerate(boletins):
    print(f'{c:<6}{b[0]:<10} {b[2]:>10}')
print('-' * 40)

while True:
    pesquisa = str(input('Mostrar notas de qual aluno? (999 ou "Para" interrompe): ')).strip().title()
    if pesquisa.isnumeric():
        pesquisa = int(pesquisa)

    if pesquisa == 'Para' or pesquisa == 999:
        break

    encontrado = False
    for c, a in enumerate(boletins):
        if isinstance(pesquisa, str):
            if pesquisa == a[0]:
                print(f'Notas de {a[0]} são {a[1]}')
                encontrado = True
                break
        else:
            if isinstance(pesquisa, int):
                if pesquisa == c:
                    print(f'Notas de {a[0]} são {a[1]}')
                    encontrado = True
                    break
    if not encontrado:
        print('Digite uma opção válida.')

    print('-' * 40)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
