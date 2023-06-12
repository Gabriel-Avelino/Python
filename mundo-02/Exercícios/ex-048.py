soma = 0
index = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        index += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(index, soma))
