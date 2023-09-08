valores = []

while True:
    valores.append(int(input('Digite uma valor: ')))

    if 5 in valores:
        msg = 'faz parte da'
    else:
        msg = 'não foi encontrado na'

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

valores.sort(reverse=True)
print('-=' * 30)
print(f'''Você digitou {len(valores)} elementos
Os valores em ordem decrescente são {valores}
O valor 5 {msg} lista!''')
