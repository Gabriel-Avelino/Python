teste = list()
teste.append('Gabriel')
teste.append(19)
pessoas = []
pessoas.append(teste[:])

print(pessoas)

teste[0] = 'Maria'  # Se não fizer uma cópia, altera o valor das duas estruturas
teste[1] = 22  # Se não fizer uma cópia, altera o valor das duas estruturas
pessoas.append(teste[:])
print(pessoas)
