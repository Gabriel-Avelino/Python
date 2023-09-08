aluno = {'Nome': str(input('Nome: ')).strip().title()}

aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
