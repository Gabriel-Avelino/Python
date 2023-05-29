n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

print('Sua média foi {}'.format(media))

print('Parabéns! Você teve uma média boa!' if media >= 6.0 else 'Você teve uma média ruim... Estude mais!')
