pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
print(pessoas)  # {'nome': 'Gustavo', 'idade': 22}

pessoas['nome'] = 'Leandro'
print(pessoas)  # {'nome': 'Leandro', 'idade': 22}

pessoas['peso'] = 98.5
print(pessoas)  # {'nome': 'Leandro', 'idade': 22, 'peso': 98.5}
