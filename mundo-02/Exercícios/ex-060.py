from  time import  sleep
print('{:^30}'.format('Usando while'))
print('=-=' * 10, '\n')

num = int(input('Digite um número para \ncalcular seu fatorial: '))
c = num
result = 1
conta = ''

while c > 0:
    conta += '{} {}'.format(c, 'x ' if c > 1 else '=')
    result *= c
    c -= 1
print('Calculando {}! = {} {}\n'.format(num, conta, result))
print('=-=' * 10)
sleep(2)

print('{:^30}'.format('Usando for'))
print('=-=' * 10, '\n')

num = int(input('Digite um número para \ncalcular seu fatorial: '))
result = 1
conta = ''

for c in range(num, 0, -1):
    conta += '{} {}'.format(c, 'x ' if c > 1 else '=')
    result *= c
print('Calculando {}! = {} {}\n'.format(num, conta, result))
