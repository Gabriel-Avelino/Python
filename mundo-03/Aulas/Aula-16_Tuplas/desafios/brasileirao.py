times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Bragantino', 'Santos', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América-MG', 'Vasco da Gama', 'Coritiba')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)

print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 15)

print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)

print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)

if 'Chapecoense' in times:
    print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
else:
    print('O Chapecoense não está nessa Série.')
