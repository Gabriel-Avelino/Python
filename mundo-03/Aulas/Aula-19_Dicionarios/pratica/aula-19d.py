Brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

Brasil.append(estado1)
Brasil.append(estado2)

print(estado1)  # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado2)  # {'uf': 'São Paulo', 'sigla': 'SP'}
print(Brasil)  # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(Brasil[0])  # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(Brasil[1])  # {'uf': 'São Paulo', 'sigla': 'SP'}
print(Brasil[0]['uf'])  # Rio de Janeiro
print(Brasil[1]['sigla'])  # SP
