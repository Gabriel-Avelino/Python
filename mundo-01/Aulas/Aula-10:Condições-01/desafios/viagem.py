distancia = float(input('Digite a distância da sua viagem em km: '))

if distancia <= 200:
    print('O valor total da viagem será R${:.2f}'.format(distancia * 0.5))
else:
    print('O valor total da viagem será R${:.2f}'.format(distancia * 0.45))
