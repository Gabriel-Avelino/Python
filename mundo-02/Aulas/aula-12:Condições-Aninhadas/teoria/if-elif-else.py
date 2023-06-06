# Uma estrutura de repetição aninhada é uma estrutura de repetição que possui mais de dois caminhos.
# Para representá-la no python, usamos o comando elif para as condições adicionais:
nome = str(input('Digite seu nome: '))

if nome == 'Gabriel':
    print('Olá, Gabriel! Bem-vindo de volta!')
elif nome == 'Zeca':
    print('O que você está fazendo aqui?')  # É possível utilizar a quantos elifs quisermos.
else:
    print('Quem é você?')
