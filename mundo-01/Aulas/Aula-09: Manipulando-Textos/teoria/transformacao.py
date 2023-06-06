# A transformção é outra das formas de manipulação de strings, através dela é possível alterar uma parte de uma string.
frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android'))  # Altera o valor de uma parte da string.
print(frase.upper())  # Deixa toda a string em letras maiúsculas.
print(frase.lower())  # Deixa toda a string em letras minúsculas.
print(frase.capitalize())  # Deixa todos os caracteres minúsculos e coloca a primeira letra em maiúsculo.
print(frase.title())  # Deixa todos os caracteres em letra minúscula e a primeira letra de cada palavra maiúscula.

frase = '  Aprenda Python  '
print(frase)
print(frase.strip())  # Remove os espaços em branco no início e no final da cadeia que não estão sendo utilizados.
print(frase.rstrip())   # Remove os espaços em branco que estão a direita da cadeia que não estão sendo utilizados.
print(frase.lstrip())   # Remove os espaços em branco que estão a esquerda da cadeia que não estão sendo utilizados.
