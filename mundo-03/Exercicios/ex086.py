matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor para [{c}, {i}]: '))

print('-=' * 30)

for c, l in enumerate(matriz):
    for i, e in enumerate(l):
        print(f'[ {e:^5} ]', end=' ')
    print()
