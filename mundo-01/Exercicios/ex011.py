largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
area = largura * altura

print('Sua parede com dimensão de {}x{} tem área de {}m². \nPara pintar essa parede, você precisará de {}l de tinta'.format(largura, altura, area, area / 2))
