maisDe18 = 0
homens = 0
mulheresMenos20 = 0
sexo = ''
continuar = ''

while True:
    print('-' * 40)
    print('{:^40}'.format('CADASTRE UMA PESSOA'))
    print('-' * 40)
    idade = int(input('Idade: '))
    while sexo not in ['M', 'F']:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        maisDe18 += 1

    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresMenos20 += 1

    sexo = ''

    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar not in ['S', 'N']:
            print('Digite uma opção válida')

    if continuar == 'N':
        break
    else:
        continuar = ''

print(f'''Total de pessoas com mais de 18 anos: {maisDe18}
Ao todo temos {homens} homens cadastrados
E temos {mulheresMenos20} mulheres com menos de 20 anos''')
