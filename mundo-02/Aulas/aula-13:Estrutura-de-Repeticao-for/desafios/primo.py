num = int(input('Digite um número inteiro: '))
multiplo = 0
for c in range(2, num):
    if num % c == 0:
        multiplo += 1
if multiplo == 0:
    print('{} é um número primo'.format(num))
else:
    print('{} não é um número primo'.format(num))
