from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade'''.format(maior, menor))
