n = int(input('Quantidade de Elemnetos: '))
c = 1
primeiroAnterior = 0
segundoAnterior = 0
while c <= n:
    if c == 1:
        fibonacci = 0
    elif c == 2:
        fibonacci = 1
        primeiroAnterior = fibonacci
    elif c == 3:
        fibonacci = 1
        segundoAnterior = primeiroAnterior
        primeiroAnterior = fibonacci

    else:
        fibonacci = primeiroAnterior + segundoAnterior
        segundoAnterior = primeiroAnterior
        primeiroAnterior = fibonacci
    print(fibonacci, end=' → ')
    c += 1
print('...')
