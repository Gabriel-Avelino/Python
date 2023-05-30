# Os códigos de estilo do terminal são formados pela seguinte estrutura:
# \033[<números 0, 1, 4 ou 7>;<números de 30 a 37 (para branco use 97)>;<números de 40 a 47>m
# Para aplicar o estilo, basta fazer da seguinte forma:

velocidade = float(input('\033[0;34mQual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('''\033[0;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h
Você deve pagar uma multa de R${:.2f}'''.format(multa))

print('\033[1;33mTenha um bom dia! Dirija com segurança!')
