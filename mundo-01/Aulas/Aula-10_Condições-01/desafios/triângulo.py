a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if b - c < a < b + c and c - a < b < c + a and b - a < c < b + a:
    print('As retas {}, {} e {} formam um triângulo'.format(a, b, c))
else:
    print('As retas {}, {} e {} não formam um triângulo'.format(a, b, c))
