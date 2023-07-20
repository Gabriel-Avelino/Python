print('{:^10}'.format('Gerador de PA'))
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 1

while c < 11:
    termo = primeiro + (c - 1) * razao
    print(termo, end=' → ')
    c += 1
print('FIM')
