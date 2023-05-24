medida = float(input('Digite a medida em metros: '))

print('A distância de {}m corresponde a: \nQuilômetro: {}km \nHectômetro: {}hm \nDecâmetro: {}dam \nDecímetro: {}dm \nCentímetro: {}cm \nMilímetro: {}mm'.format(medida, (medida / 1000), (medida / 100), (medida / 10), (medida * 10), (medida * 100), (medida * 1000)))
