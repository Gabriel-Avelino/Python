from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))

print('O comprimento da hipotenusa é: {}'.format(hypot(oposto, adjacente)))
