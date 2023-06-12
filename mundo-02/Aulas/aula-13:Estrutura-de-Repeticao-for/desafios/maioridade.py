from datetime import date
maior = 0
menor = 0

for c in range(0, 7):
    pessoa = int(input('Digite o ano de nascimento da pessoa: '))

    if date.today().year - pessoa >= 21:
        maior += 1
    else:
        menor += 1

print('Há {} maiores de idade e {} menores de idade.'.format(maior, menor))
