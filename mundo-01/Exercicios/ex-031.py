distancia = float(input('Qual é a distância da sua viagem? '))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print('''Você está prestes a começar uma viagem de {}Km
E o preço  da sua passagem será de R${:.2f}'''.format(distancia, passagem))
