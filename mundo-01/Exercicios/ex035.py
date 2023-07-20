print('-=-' * 20, '\nAnalisador de Triângulos')
print('-=-' * 20)

a = float(input('Primeiro Segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if b - c < a < b + c and c-a < b < c+a and b-a < c < b+a:
    print('Os segmentos {}, {} e {} podem formar um triângulo'.format(a, b, c))
else:
    print('Os segmentos {}, {} e {} não podem formar um triângulo'.format(a, b, c))
