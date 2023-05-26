num = input('Digite um número entre 0 e 9999: ')
unidades = num.replace('', ' ').split()

print('Analisando o número {0} \nUnidade: {4} \nDezena: {3} \nCentena: {2} \nMilhar: {1}'.format(num, unidades[0], unidades[1], unidades[2], unidades[3]))
