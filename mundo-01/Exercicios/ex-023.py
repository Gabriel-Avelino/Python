num = int(input('Digite um número entre 0 e 9999: '))

print('Analisando o número {} \nUnidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(num, num//1 % 10, num//10% 10, num//100 % 10, num//1000 % 10))
