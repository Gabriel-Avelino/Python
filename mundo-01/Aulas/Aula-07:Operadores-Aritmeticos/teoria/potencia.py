# Entre os operadores também há o da potência(**), que eleva o valor de um número pelo outro:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 ** n2

print('A potência de {} elevado a {} resulta em {}'.format(n1, n2, s))

# Outra forma de representar potência é usando o método pow():
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = pow(n1, n2)

print('A potência de {} elevado a {} resulta em {}'.format(n1, n2, s))

# Obs: Caso quisermos uma raiz, basta passar uma fração ou um número decimal como expoente.
