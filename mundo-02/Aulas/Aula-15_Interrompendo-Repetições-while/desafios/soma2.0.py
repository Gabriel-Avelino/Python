s = 0
c = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))

    if num == 999:
        break
    s += num
    c += 1
print(f'A soma dos {c} valores foi {s}!')
