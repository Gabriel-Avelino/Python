print('-' * 30)
print('{:^30}'.format('Sequência de Fibonacci'))
print('-' * 30)

termos = int(input('Quantos termos você quer mostrar? '))
print('~' * 30)
c = 1
anterior = 0
segundoAnterior = 0
elemento = 0

while c <= termos:
    if c == 1:
        anterior = elemento
    elif c == 2:
        elemento = 1
        segundoAnterior = anterior
        anterior = elemento
    else:
        elemento = anterior + segundoAnterior
        segundoAnterior = anterior
        anterior = elemento
    print(elemento, end=' → ')
    c += 1
print('FIM')
print('~' * 30)
