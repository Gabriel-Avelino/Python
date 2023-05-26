num = int(input('Digite um número inteiro entre 0 e 9999: '))

print('''O número digitado foi {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar {}'''.format(num, num//1 % 10, num//10 % 10, num//100 % 10, num//1000 % 10))
