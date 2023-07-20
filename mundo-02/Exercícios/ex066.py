c = 0
soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))

    if num == 999:
        break
    c += 1
    soma += num

print(f'A soma dos {c} valores foi {soma}!')
