# Também há métodos no Python que permitem verificar os tipos de variáveis, são os métodos is. Veja alguns exemplos:
n1 = input('Digite algo: ')

print(n1.isnumeric())  # Verifica se é possível converter o valor em um número.

# ----------

n2 = input('Digite algo: ')

print(n2.isalpha())  # Verifica se é uma letra.

# ----------

n3 = input('Digite algo: ')

print(n3.isalnum())  # Verifica se é um valor alfanumérico.

# ----------

n4 = input('Digite algo: ')

print(n4.isupper())  # Verifica se o valor possui apenas letras maiúsculas.
