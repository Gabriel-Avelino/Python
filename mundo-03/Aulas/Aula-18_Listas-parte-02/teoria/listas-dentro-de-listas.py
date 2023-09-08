# É possível armazenar listas dentro de uma lista maior. Basta fazer da seguinte forma:
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)

# É possível também colocar uma lista dentro de outra através do método append:
cliente1 = ['Juscelino', 47]
cliente2 = ['Paulo', 36]
pessoas.append(cliente1[:])
pessoas.append(cliente2[:])
print(pessoas)

# Podemos acessar os dados individuais dessas listas da seguinte forma:
print(pessoas[0][0])  # Pedro
print(pessoas[1][1])  # 19
print(pessoas[2][0])  # João
print(pessoas[1])  # ['Maria', 19]
