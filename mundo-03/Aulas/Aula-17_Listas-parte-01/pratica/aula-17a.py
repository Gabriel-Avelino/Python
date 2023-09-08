num = [2, 5, 9, 1]
print(num)

num[2] = 3
print(num)

# num [4] = 7  # Gera erro
num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(2, 0)
print(num)

num.pop()
print(num)

num.pop(2)
print(num)

num.insert(2, 2)
print(num)

num.remove(2)  # Remove a primeira ocorrência na lista
print(num)

# num.remove(4)  # Gera um erro

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')
