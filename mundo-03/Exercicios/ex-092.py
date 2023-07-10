from datetime import datetime

ficha = {}

ficha['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de Nascimento: '))
ficha['idade'] = datetime.now().year - nascimento

while True:
    carteira = int(input('Carteira de Trabalho (0 não tem): '))
    if carteira < 0:
        print('Digite um número válido! ')
    else:
        ficha['ctps'] = carteira
        break

if ficha['ctps'] > 0:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['salário'] = float(input('Salário: R$'))
    aposentar = ficha['idade'] + ((ficha['contratação'] + 35) - datetime.now().year)
    ficha['aposentadoria'] = aposentar

for k, v in ficha.items():
    print(f'    - {k} tem o valor {v}')
