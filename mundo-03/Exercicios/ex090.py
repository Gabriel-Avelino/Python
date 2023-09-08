ficha = dict()

ficha['nome'] = str(input('Nome: ')).strip().title()
ficha['média'] = float(input(f'Média de {ficha["nome"]}: '))

if ficha['média'] >= 7:
    ficha['situação'] = 'Aprovado'
elif ficha['média'] > 5:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado'

print('-=' * 30)
for k, v in ficha.items():
    print(f'''  - {k} é igual a {v}''')
