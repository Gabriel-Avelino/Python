classificados = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Atlético-MG', 'Fluminense', 'São Paulo',
                 'Internacional', 'Bragantino', 'Fortaleza', 'Athletico-PR', 'Cruzeiro', 'Santos', 'Bahia',
                 'Corinthians', 'Cuiabá', 'Goiás', 'América-MG', 'Vasco da Gama', 'Coritiba')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {classificados}')
print('-=' * 15)

print(f'Os 5 primeiros são {classificados[:5]}')
print('-=' * 15)

print(f'Os 4 últimos são {classificados[-4:]}')
print('-=' * 15)

print(f'Times em ordem alfabética: {sorted(classificados)}')

print('-=' * 15)

if 'Chapecoense' in classificados:
    print(f'O Chapecoense está na {classificados.index("Chapecoense") + 1}ª posição')
else:
    print('O Chapecoense não está classificado nessa série.')
