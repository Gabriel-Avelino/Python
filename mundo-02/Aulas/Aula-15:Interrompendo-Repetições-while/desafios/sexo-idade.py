maior = 0
homens = 0
mulheresMenos20 = 0
continuar = ''
sexo = ''

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    while sexo not in ['M', 'F']:
        sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
        if sexo not in ['M', 'F']:
            print('Digite um sexo válido')
    idade = int(input('Digite sua idade: '))
    print('-' * 30)

    if idade > 18:
        maior += 1

    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            mulheresMenos20 += 1
    while continuar not in ['S', 'N']:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    continuar = ''
    sexo = ''

print(f'''{maior} pessoas têm mais de 18 anos.
{homens} homens foram cadastrados.
{mulheresMenos20} mulheres têm menos de 20 anos.''')
