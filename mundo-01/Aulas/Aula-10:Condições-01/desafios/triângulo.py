a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if b-c < a < b + c:
    print('As retas {}, {} e {} formam um triângulo'.format(a, b, c))
else:
    print('As retas {}, {} e {} não formam um triângulo'.format(a, b, c))
