peso = float(input('\033[35mQual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'
         }

imc = peso / (altura ** 2)

print('{1}O IMC dessa pessoa é de {0:.1f}'. format(imc, cores['ciano']))
if imc < 18.5:
    print('{}Você está ABAIXO DO PESO normal'.format(cores['azul']))
elif 18.5 <= imc < 25:
    print('{}PARABÉNS, você está na faixa de PESO NORMAL'.format(cores['verde']))
elif 25 <= imc < 30:
    print('{}Você está em SOBREPESO!'.format(cores['amarelo']))
elif 30 <= imc < 40:
    print('{}Você está em OBESIDADE!'.format(cores['vermelho']))
else:
    print('{}Você está em OBESIDADE MÓRBIDA, cuidado!'.format(cores['cinza']))
