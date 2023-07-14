estado = dict()
Brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip().title()
    estado['sigla'] = str(input('Sigla: ')).strip().upper()
    # Brasil.append(estado[:])  # Gera erro
    Brasil.append(estado.copy())
# print(Brasil)  # [{'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Rio De Janeiro', 'sigla': 'RJ'}, {'uf': 'Paraná', 'sigla': 'PR'}]
for e in Brasil:
    # print(e)
    # {'uf': 'São Paulo', 'sigla': 'SP'}
    # {'uf': 'Rio De Janeiro', 'sigla': 'RJ'}
    # {'uf': 'Paraná', 'sigla': 'PR'}

    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    print()

for est in Brasil:
    for v in est.values():
        print(v, end=' ')
    print()
