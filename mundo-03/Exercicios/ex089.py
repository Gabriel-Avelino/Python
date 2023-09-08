from unidecode import unidecode
boletins = []
aluno = []
notas = []

while True:
    nome = str(input('Nome: ')).strip().title()
    aluno.append(nome)

    for c in range(1, 3):
        notas.append(float(input(f'Nota {c}: ')))
    aluno.append(notas[:])

    soma = 0
    for n in notas:
        soma += n
    media = soma / len(notas)

    aluno.append(media)
    boletins.append(aluno[:])
    aluno.clear()
    notas.clear()

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10} {"MÉDIA":>8}')
print('-' * 26)

for c, b in enumerate(boletins):
    print(f'{c + 1:<4}{b[0]:<10} {b[2]:>8}')

while True:
    print('-' * 35)
    pesquisa = str(input('Mostrar notas de qual aluno? (999 ou "Para" interrompe): ')).strip().title()
    if pesquisa.isnumeric():
        pesquisa = int(pesquisa)

    if pesquisa == 'Para' or pesquisa == 999:
        break

    encontrado = ''
    for c, a in enumerate(boletins):
        if isinstance(pesquisa, str):
            if pesquisa == unidecode(a[0]):
                print(f'Notas de {a[0]} são {a[1]}')
                encontrado = True
        elif isinstance(pesquisa, int):
            if pesquisa - 1 == c:
                print(f'Notas de {a[0]} são {a[1]}')
                encontrado = True
    if not encontrado:
        print('Digite uma opção válida')

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
