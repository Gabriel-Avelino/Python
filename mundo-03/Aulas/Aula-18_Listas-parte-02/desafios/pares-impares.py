nums = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
nums[0].sort()
nums[1].sort()
print(f'''Os valores pares digitados foram: {nums[0]}
Os valores ímpares digitados foram: {nums[1]}''')
