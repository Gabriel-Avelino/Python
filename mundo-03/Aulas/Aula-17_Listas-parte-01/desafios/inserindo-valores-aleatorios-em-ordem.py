valores = []

for c in range(5):
    num = int(input('Digite um valor: '))

    if not valores:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        for i, v in enumerate(valores):
            if num < v:
                valores.insert(i, num)
                print(f'Adicionado na posição {valores.index(num)} da lista...')
                break
        else:
            valores.append(num)
            print('Adicionado ao final da lista...')
print('=-' * 40)
print(f'Os valores digitados em ordem foram {valores}')
