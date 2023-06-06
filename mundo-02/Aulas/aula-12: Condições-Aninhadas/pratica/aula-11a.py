nome = str(input('Qual é o seu nome? '))

if nome == 'Gabriel':
    print('Seu nome é o mesmo que o meu!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal')  # Lembrando que o else é uma estrutura opcional.
print('Tenha um bom dia, {}!'.format(nome))
