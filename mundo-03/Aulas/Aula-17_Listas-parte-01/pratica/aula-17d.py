a = [2, 3, 4, 7]
b = a
b[2] = 8  # Muda ambas as listas

print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:]  # Cria cópia de 'a'
b[2] = 8  # Muda somente a lista b

print(f'Lista A: {a}')
print(f'Lista B: {b}')
