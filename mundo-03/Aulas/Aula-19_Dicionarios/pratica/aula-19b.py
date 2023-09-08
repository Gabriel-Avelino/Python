pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k in pessoas.keys():
    print(k)
    # nome
    # sexo
    # idade

for v in pessoas.values():
    print(v)
    # Gustavo
    # M
    # 22

for k, v in pessoas.items():
    print(f'{k} = {v}')
    # nome = Gustavo
    # sexo = M
    # idade = 22
