inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

if inicio % 2 == 0 and razao % 2 == 0 or inicio % 2 != 0 and razao % 2 != 0:
    i = 11
else:
    i = 10

for c in range(inicio, i * razao, razao):
    print(c)
print('FIM')
