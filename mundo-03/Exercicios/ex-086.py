matriz = []
linha = []

for c in range(0, 3):
    for i in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{c}, {i}]: ')))
    matriz.append(linha[:])
    linha.clear()

print('-=' * 30)

for c, l in enumerate(matriz):
    for i, e in enumerate(l):
        print(f'[ {e:^5} ]', end=' ')
    print()
