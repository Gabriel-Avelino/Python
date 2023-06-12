print('=' * 40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

for c in range(primeiro, razao * 10, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')
