soma = 0
index = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número inteiro: '.format(c)))
    if num % 2 == 0:
        soma += num
        index += 1
print('Você informou {} número(s) par(es) e a soma foi: {}'.format(index, soma))
