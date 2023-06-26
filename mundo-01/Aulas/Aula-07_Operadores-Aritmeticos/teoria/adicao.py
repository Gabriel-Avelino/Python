# Os operadores aritméticos têm o objetivo de realizar contas matemáticas.
# O operador de adição (+) é o primeiro deles, ele possui a função de somar dois valores:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2

print('A soma entre {} e {} resulta em {}'.format(n1, n2, s))

# Obs: A ordem precedência entre as operações segue a mesma da matemática:
# 1° parênteses (lembrando que em Python não utilizamos colchetes e chaves para operações)
# 2° potência
# 3° multiplicação, divisão, divisão inteira e resto da divisão
# 4° adição e subtração
