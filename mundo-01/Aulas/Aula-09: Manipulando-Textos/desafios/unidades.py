num = input('Digite um número inteiro entre 0 e 9999: ').strip()

separado = num.replace('', ' ').split()
print('''O número digitado foi {0}
Unidade: {4}
Dezena: {3}
Centena: {2}
Milhar {1}'''.format(num, separado[0], separado[1], separado[2], separado[3]))
