valores = []

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if not valores or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        for i, v in enumerate(valores):
            if num <= v:
                valores.insert(i, num)
                print(f'Adicionado na posição {i} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
