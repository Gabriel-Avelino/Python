num = int(input('Digite um número inteiro entre 0 e 9999: ')).strip()

print('''O número digitado foi {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar {}'''.format(num, separado[0], separado[1], separado[2], separado[3]))
