nome = str('Qual é o seu nome? ')

if nome == 'Gabriel':
    print('Seu nome é o mesmo que o meu!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!'.format(nome))
