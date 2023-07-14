pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas[0])  # Isso gera um erro
print(pessoas['nome'])  # Gustavo
print(pessoas['idade'])  # 22
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())  # dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values())  # dict_values(['Gustavo', 'M', 22])
print(pessoas.items())  # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
