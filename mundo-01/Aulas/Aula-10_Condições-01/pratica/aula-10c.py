n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

print('Sua média foi {}'.format(media))

if media >= 6.0:
    print('Parabéns! Você teve uma média boa!')
else:
    print('Você teve uma média ruim... Estude mais!')
