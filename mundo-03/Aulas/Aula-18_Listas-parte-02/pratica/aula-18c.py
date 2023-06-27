pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in pessoas:
    print(p)  # Todas as listas

print('\n')

for p in pessoas:
    print(p[0])  # Todos os nomes

print('\n')

for p in pessoas:
    print(p[1])  # Todos as idades

print('\n')

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')  # Todos as idades
