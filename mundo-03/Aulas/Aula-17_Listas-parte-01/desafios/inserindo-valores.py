valores = []

while True:
    numero = int(input('Digite um valor: '))

    valores.append(numero)

    while True:
        continuar = ''
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in ['N', 'S']:
            break
    if continuar == 'N':
        break
print('-=' * 30)
valores.sort(reverse=True)
print(f'''Você digitou {len(valores)} elementos.
Os valores em ordem decrescente são {valores}''')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
