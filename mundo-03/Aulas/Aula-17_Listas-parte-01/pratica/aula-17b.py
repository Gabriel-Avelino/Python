valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...', end=' ')
print('\n')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
