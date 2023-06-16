num = c = soma = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        c += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(c, soma))
