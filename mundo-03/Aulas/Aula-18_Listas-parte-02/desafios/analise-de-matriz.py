matriz = []
linha = []
somaPares = 0
somaColuna3 = 0
maiorNumLinha2 = 0

for c in range(0, 3):
    for i in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{c}, {i}]: ')))
    matriz.append(linha[:])
    linha.clear()

print('-=' * 30)

for c, l in enumerate(matriz):
    for i, e in enumerate(l):
        print(f'[{e:^5}]', end=' ')
        if e % 2 == 0:
            somaPares += e
        if i == 2:
            somaColuna3 += e
        if c == 1 and e > maiorNumLinha2:
            maiorNumLinha2 = e
    print()

print('-=' * 30)

print(f'''A soma dos valores pares é {somaPares}.
A soma dos valores da terceira coluna é {somaColuna3}.
O maior valor da segunda linha é {maiorNumLinha2}.''')
