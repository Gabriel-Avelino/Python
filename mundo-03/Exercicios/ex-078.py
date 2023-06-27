valores = []
maior = 0
menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-' * 30)
print(f'Você digitou os valores {valores}')

for p, n in enumerate(valores):
    if p == 0:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}...', end=' ')
