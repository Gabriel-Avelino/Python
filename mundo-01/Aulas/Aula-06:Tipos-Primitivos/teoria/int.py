# Na aula 04, houve um desafio de soma, onde ocorria um erro em que ao invés de somar os dois valores, o python os concatenava.
# Para corrigir, basta declarar o tipo de variável usando um dos quatro tipos primitivos, o 'int':
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2

print('A soma vale {}'.format(s))
