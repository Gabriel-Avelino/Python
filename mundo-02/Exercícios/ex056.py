soma = 0
maisVelho = ''
idadeVelho = 0
menosVinte = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    soma += idade

    if sexo == 'M' and idade > idadeVelho:
        idadeVelho = idade
        maisVelho = nome
    elif sexo == 'F' and idade < 20:
        menosVinte += 1

print('''A média de idade do grupo é de {} anos.
O homem mais velho tem {} anos e se chama {}.
Ao todo são {} mulheres com menos de 20 anos.'''.format(soma / 4, idadeVelho, maisVelho, menosVinte))
