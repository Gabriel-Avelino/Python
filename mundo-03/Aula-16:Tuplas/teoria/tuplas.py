# No python é possível criar variáveis compostas que podem receber mais de um valor. Exitem três tipos de variáveis compostas, as tuplas são um deles, e possuem a seguinte estrutura:
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'  # Na versão antiga do Python, seus valores eram declarados entre parênteses.

# Cada um dos valores é organizado índices numerados a partir de 0, e podemos acessá-los da seguinte forma:
print(lanche)  # ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[0])  # Hambúrguer
print(lanche[1])  # Suco
print(lanche[2])  # Pizza
print(lanche[3])  # Pudim

print(lanche[-1])  # Pudim
print(lanche[-2])  # Pizza
print(lanche[-3])  # Suco
print(lanche[-4])  # Hambúrguer

# Também é possível usar fatiamentos com tuplas:
print(lanche[0:2])  # ('Hambúrguer', 'Suco')
print(lanche[1:])  # ('Suco', 'Pizza', 'Pudim')

# É possível usar o método len() nas tuplas:
print(len(lanche))  # 4

# Outra possibilidae, é utilizar o método for para mostrar cada um dos elementos das variáveis compostas:
for c in lanche:
    print(c, end=' ')

# Obs: não é possível alterar os valores de tuplas, porque tuplas são imutáveis.
