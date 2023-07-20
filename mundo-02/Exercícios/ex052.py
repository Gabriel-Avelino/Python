num = int(input('Digite um número: '))
multiplo = 0
divisivel = 0

i = 0

for c in range(1, num + 1):
    if num % c == 0:
        multiplo += 1
        divisivel += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if multiplo == 2:
    print('''\n\033[mO número {} foi divisível {} vezes
E por isso ele É PRIMO!'''.format(num, divisivel))
else:
    print('''\n\033[mO número {} foi divisível {} vezes
E por isso ele NÃO É PRIMO!'''.format(num, divisivel))
