# Os dicionários são estruturas de dados semelhantes a tuplas e listas, porém, possuem índices literais. São declarados da seguinte forma:
# dados = dict()

# Também é possível criar um dicionário preenchido da seguinte forma:
dados = {'Nome': 'Gabriel', 'Idade': 19}

# Para mostrar os dados, basta usar o índice literal
print(dados['Nome'])  # Gabriel
print(dados['Idade'])  # 19

# Não utilizamos append ara adicionar dados em um dicionário, no lugar utilizamos a seguinte estrutura:
dados['Sexo'] = 'M'
print(dados)  # {'Nome': 'Gabriel', 'Idade': 19, 'Sexo': 'M'}

# Para deletar, usamos o comando del:
del dados['Idade']
print(dados)  # {'Nome': 'Gabriel', 'Sexo': 'M'}

# Também é possível criar dicionários da seguinte forma:
filme0 = {'Título': 'Star Wars',
          'Ano': 1977,
          'Diretor': 'George Lucas'
          }

# Os índices literais são chamados de chaves/keys. A qualquer momento é possível acessar itens, chaves e valores:
print(filme0.values())  # dict_values(['Star Wars', 1977, 'George Lucas'])
print(filme0.keys())  # dict_keys(['Título', 'Ano', 'Diretor'])
print(filme0.items())  # dict_items([('Título', 'Star Wars'), ('Ano', 1977), ('Diretor', 'George Lucas')])

# Esses conceitos também podem ser usados com o for:
for k, v in filme0.items():
    print(f'O {k} é {v}')
    # O Título é Star Wars
    # O Ano é 1977
    # O Diretor é George Lucas

# Também é possível unir listas, tuplas e dicionários:
locadora = []
locadora.append(filme0)
filme1 = {'Título': 'Avengers',
          'Ano': 2012,
          'Diretor': 'Joss Whedon'
          }
locadora.append(filme1)

filme2 = {'Título': 'Avengers',
          'Ano': 2012,
          'Diretor': 'Joss Whedon'
          }
locadora.append(filme2)

print(locadora[0]['Ano'])  # 1977
print(locadora[1]['Diretor'])  # Joss Whedon
print(locadora[2]['Título'])  # Avengers
