matriz = []
linha = []
somaPares = 0
somaColuna3 = 0
maiorValorLinha2 = 0

for c in range(0, 3):

    for i in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{c}, {i}]: ')))

    matriz.append(linha[:])
    linha.clear()

print('-=' * 30)
for c, l in enumerate(matriz):

    for i, e in enumerate(l):
        if c > 0 and i == 0:
            print(f'\n[ {e} ]', end=' ')
        else:
            print(f'[ {e} ]', end=' ')

        if e % 2 == 0:
            somaPares += e

        if i == 2:
            somaColuna3 += e

        if c == 1 and e > maiorValorLinha2:
            maiorValorLinha2 = e

print(f'\n{"-=" * 30}')
print(f'''A soma dos valores pares é {somaPares}.
A soma dos valores da terceira coluna é {somaColuna3}.
O maior valor da segunda linha é {maiorValorLinha2}.''')
