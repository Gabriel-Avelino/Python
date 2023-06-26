inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
enesimo = inicio + (11 - 1) * razao

for c in range(inicio, enesimo, razao):
    print(c)
print('FIM')
