# Se quisermos uma variável composta onde conseguimos mudar as informações, usamos listas. Elas possuem a seguinte estrutura:
lanche = ['hambúrguer', 'suco', 'pizza', 'pudim']
print(lanche[3])
lanche[3] = 'picolé'
print(lanche)

# Para adicionar um novo elemento ao final de uma lista, usamos o seguinte comando:
lanche.append('cookie')
print(lanche)

# Agora, para adicionar um novo elemento em um determinado espaço da lista sem retirar os elementos existentes, usamos o seguinte comando:
lanche.insert(0, 'cachorro-quente')
print(lanche)

# Para remover o item de uma lista, é possível usar três métodos, del, pop e remove:

del lanche[3]
lanche.pop()  # Remove o último item da lista, porém, é possível usar o índice para remover um item específico.
lanche.remove('suco')

print(lanche)

# Ao tentar remover um item inexistente, o programa retorna um erro, para resolver isso, basta usar um if:
if 'suco' in lanche:
    lanche.remove('suco')
print(lanche)

# Também é possível criar uma lista usando range:
valores = list(range(4, 11))  # [4, 5, 6, 7, 8, 9, 10]
print(valores)

# Caso quisermos uma lista desordenada, criamos através do método padrão:
nums = [8, 2, 5, 4, 9, 3, 0]
print(nums)

# Se quisermpos orgar esses valores, usamos o método sort:
nums.sort()
print(nums)

# Para conseguir a ordem inversa, usamos o método sort, acompanhado do parâmetro reverse:
nums.sort(reverse=True)
print(nums)

# Também é possível saber o tamanho de uma lista usando o len():
print(len(valores))
