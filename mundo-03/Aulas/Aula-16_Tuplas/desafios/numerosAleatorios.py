from random import random
c = 0
maior = 0
menor = -1

num = (int(random()*10), int(random()*10), int(random()*10), int(random()*10), int(random()*10))

while c < len(num):
    if num[c] > maior:
        maior = num[c]
    if num[c] < menor or menor == -1:
        menor = num[c]
    c += 1

print(f'''O valores sorteados foram: {num[0]} {num[1]} {num[2]} {num[3]} {num[4]}
O maior valor sorteado foi {maior}
O menor valor sorteado foi {menor}''')
