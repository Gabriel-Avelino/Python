num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 > num3:
    print('O maior número é {}'.format(num1))
elif num2 > num1 > num3:
    print('O maior número é {}'.format(num2))
else:
    print('O maior número é {}'.format(num3))

if num1 < num2 < num3:
    print('O menor número é {}'.format(num1))
elif num2 < num1 < num3:
    print('O menor número é {}'.format(num2))
else:
    print('O menor número é {}'.format(num3))
