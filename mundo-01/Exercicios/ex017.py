from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format(hypot(oposto, adjacente)))

# É possível também resolver o mesmo exercício sem importações:
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format((co ** 2 + ca ** 2) ** (1/2)))
