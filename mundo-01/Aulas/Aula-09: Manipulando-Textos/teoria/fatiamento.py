# As strings (também conhecidas como cadeias de caracteres) são textos que podem ser passados para variáveis ou diretamente para o usuário:
frase = 'Curso em Vídeo Python.'
# Ao armazenar essa string, o Python cria pequenos espaços na memória do computador e adiciona os caracteres em cada um desses espaços.
# Essa divisão permite uma série de ações dentro dessa string.
# A primeira delas é o fatiamento, que pode ser feito de várias maneiras:
print(frase[9])  # Retorna uma letra.
print(frase[9:13])  # Retorna um pedaço pré-definido da string, excluindo o último caractere da sequência.
print(frase[9:21])  # Retorna a partir de um pedaço até o caractere final dessa nossa string.
print(frase[9:21:2])  # Retorna a partir de um pedaço até o caractere final dessa nossa string, mas pula alguns caracteres.
print(frase[:5])  # Retorna do início da string até um caractere pré-definido
print(frase[15:])  # Retorna de um ponto específico até o final da string.
print(frase[9::3])  # Retorna de um ponto específico até o final da string, pulando 3 caracteres
