matriz = []
linha = []
for c in range(0, 3):
    for i in range(0, 3):
        linha.append(int((input(f'Digite um valor para [{c}, {i}]: '))))
    matriz.append(linha[:])
    linha.clear()

print('-=' * 30)
for c, l in enumerate(matriz):
    for i, e in enumerate(l):
        if i == 0 and c > 0:
            print(f'\n{f"[ {e:^6} ]":^6}', end=' ')
        else:
            print(f'{f"[ {e:^6} ]":^6}', end=' ')

