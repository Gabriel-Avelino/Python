from datetime import date
ficha = {}

ficha['Nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de Nascimento: '))
ficha['Idade'] = date.today().year - nascimento

while True:
    carteira = int(input('Carteira de Trabalho (0 não tem): '))
    if carteira < 0:
        print('Digite um número válido!')
    else:
        ficha['CTPS'] = carteira
        break

if ficha['CTPS'] > 0:
    ficha['Contratação'] = int(input('Ano de Contratação: '))
    ficha['Salário'] = float(input('Salário: R$'))
    aposentar = (35 - (date.today().year - ficha['Contratação'])) + ficha['Idade']
    ficha['Aposentadoria'] = f'{aposentar} anos'
print('-=' * 30)
print(ficha)

for k, v in ficha.items():
    print(f'{k}: {v}')
