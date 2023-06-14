num = int(input('Digite um número: '))
c = num
result = 1
while c != 0:
    result *= c
    c -= 1
print("Fatorial de {} = {}".format(num, result))
