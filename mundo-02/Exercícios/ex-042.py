a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a - b < c < a + b and a - c < b < a + c and b - c < a < b + c:
    if a == b == c:
        tipo = 'EQUILÁTERO'
    print('Os segmentos acima PODEM um triângulo {}')

