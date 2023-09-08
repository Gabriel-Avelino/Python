nums = []
maior = 0
menor = 0
posicaoMaior = []
posicaoMenor = []

for c in range(0, 5):
    nums.append(int(input(f'Digite um valor para a posição {c}: ')))

for pos, n in enumerate(nums):
    if pos == 0:
        maior = n
        menor = n
        posicaoMaior.append(pos)
        posicaoMenor.append(pos)
    else:
        if n > maior:
            maior = n
            posicaoMaior.clear()
            posicaoMaior.append(pos)
        elif n == maior:
            posicaoMaior.append(pos)
        elif n < menor:
            menor = n
            posicaoMenor.clear()
            posicaoMenor.append(pos)
        elif n == menor:
            posicaoMenor.append(pos)
print('=-' * 30)
print(f'Você digitou os valores: {nums}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos in posicaoMaior:
    print(pos, end='')
    print('...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos in posicaoMenor:
    print(pos, end='')
    print('...', end=' ')
