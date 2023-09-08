print('=' * 40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
enesimo = primeiro + (11 - 1) * razao

for c in range(primeiro, enesimo, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')
