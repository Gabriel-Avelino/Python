from math import trunc
num = float(input('Digite um número: '))

print('O número digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

# Dá para resolvermos esse mesmo exercício sem importação também:
num = float(input('Digite um número: '))

print('O número digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
