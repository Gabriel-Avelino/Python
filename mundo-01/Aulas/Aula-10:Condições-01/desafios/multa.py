velocidade = float(input('Digite a velocidade do carro: '))
ultrapassado = velocidade - 80

if velocidade > 80:
    print('Você está a {} km/h. Ultrapassou o limite de velocidade em {} km/h e será multado em R${:.2f}'.format(velocidade, ultrapassado, ultrapassado * 7))
else:
    print('Você está a {} km/h. Está dentro do limite de velocidade.'.format(velocidade))
