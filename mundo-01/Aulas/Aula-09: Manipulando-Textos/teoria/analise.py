# Também é possível analisar uma string de diferentes maneiras:
frase = 'Curso em Vídeo Python'

print(len(frase))  # Retorna o tamanho da string.
print(frase.count('o'))  # Retorna a quantidade de vezes que aparece um caractere definido.
print(frase.count('o', 0, 13))  # Retorna a quantidade de vezes que um caractere aparece, além de já fazer o fatiamento.
print(frase.find('deo'))  # Retorna a posição de qual caractere ele encontrou uma parte da string.
print(frase.find('Android'))  # Retorna o valor -1, porque não essa string na string analisada.
print('Curso' in frase)  # Retorna um booleano que indica se a string defina existe ou não.
