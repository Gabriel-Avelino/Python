soma = 0
num = 0
c = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        c += 1
        soma += num
print('''Você digitou {} número(s)
A soma entre eles é igual a: {}'''.format(c, soma))
