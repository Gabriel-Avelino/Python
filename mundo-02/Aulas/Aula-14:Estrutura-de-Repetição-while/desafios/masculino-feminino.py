sexo = ''
while sexo not in ['M', 'm', 'F', 'f']:
    sexo = str(input('Sexo [M / F]'))
    if sexo not in 'MmFf':
        print('Digite uma opção válida')
if sexo in ['M', 'm']:
    sexo = 'MASCULINO'
elif sexo in ['F', 'f']:
    sexo = 'FEMININO'
print('Você é do sexo {}!'.format(sexo))
