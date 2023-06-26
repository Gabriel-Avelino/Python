num = int(input('Digite um número inteiro: '))

print('=' * 20)
print('TABUADA DO {}'.format(num))
print('=' * 20)
for c in range (1, 11):
    resultado = num * c
    print('{} x {} = {}'.format(num, c, resultado))
print('FIM')
