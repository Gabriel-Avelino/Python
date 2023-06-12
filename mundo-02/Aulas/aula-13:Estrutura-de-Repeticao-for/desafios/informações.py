maisVelho = ''
maiorIdade = 0
mediaIdade = 0
anos = 0

for c in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('''Qual seu sexo?: 
    [ 1 ] MASCULINO
    [ 2 ] FEMININO
    Sua opção: ''')).strip().upper()

    mediaIdade += idade

    if sexo == 'MASCULINO' or sexo == '1':
        if idade > maiorIdade:
            maiorIdade = idade
            maisVelho = nome
    if sexo == 'FEMININO' or sexo == '2':
        if idade < 20:
            anos += 1
print('''Média de idade do grupo: {:.2f}
Homem mais velho: {}
Quantidade de mulheres com menos de 20 anos: {}'''.format(mediaIdade / 4, maisVelho, anos))




