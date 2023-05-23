# Se quisermos, podemos passar parâmetros para as chaves do format para definir como ficará o texto:
nome = input('Qual seu nome? ')

print('Prazer em te conhecer {:>27}!'.format(nome))  # 27 caracteres e alinhado a direita.
print('Prazer em te conhecer {:<27}!'.format(nome))  # 27 caracteres e alinhado a esquerda.
print('Prazer em te conhecer {:^27}!'.format(nome))  # 27 caracteres e centralizado.
print('Prazer em te conhecer {:=^27}!'.format(nome))  # 27 caracteres, centralizado e adiciona o caractere digitado nos espaços restantes.
