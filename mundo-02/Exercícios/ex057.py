sexo = str(input('Informe seu sexo: [M/F} ')).strip().upper()
while sexo != 'F' and sexo != 'FEMININO' and sexo != 'M' and sexo != 'MASCULINO':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()

if sexo == 'F' or sexo == 'FEMININO':
    sexo = 'FEMININO'
elif sexo == 'M' or sexo == 'MASCULINO':
    sexo = 'MASCULINO'

print('Sexo {} registrado com sucesso'.format(sexo))
