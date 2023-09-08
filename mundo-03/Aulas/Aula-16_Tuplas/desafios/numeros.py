nums = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
pares = []
i = 0

print(f'O número 9 apareceu {nums.count(9)} vezes')

if 3 in nums:
    print(f'O número 3 apareceu pela primeira vez na {nums.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')

for c in nums:
    if c % 2 == 0:
        pares.append(c)

print(f'Os valores pares digitados foram {pares}')
