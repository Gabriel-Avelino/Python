# Entre os operadores, também há o da multiplicação(*). Esse operador tem a função de multiplicar um número pelo outro:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 * n2

print('A multiplicação entre {} e {} resulta em {}'.format(n1, n2, s))

# Caso utilizado ao lado de uma string, esse operador irá escrever ela por uma x quantidade de vezes:
string = input('Digite uma string: ')
m = int(input('Digite a quantidade de vezes que ela aparecerá: '))

r = string * m

print('A multiplicação entre {} e {} resulta em {}'.format(string, m, r))
