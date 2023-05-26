frase = 'Curso em Vídeo Python'

print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

# Bônus
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum.""")  # Se quisermos separar um texto grande em várias linhas, usamos aspas três vezes.

print(frase.count('o'))  # 3
print(frase.count('O'))  # 0
print(frase.upper().count('O'))  # 3
print(len(frase))  # 21

# Teste com espaços
frase = '  Curso em Vídeo Python  '

print(len(frase))  # 25
print(len(frase.strip()))  # 21

# De volta ao estado inicial
frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android'))  # Curso em Vídeo Android
# Obs: strings naturalmente são imutáveis, logo o replace não muda a string original, ele apenas cria uma cópia do string alterando os valores
# Para mudar uma string, nós realizamos o replace, e depois atribuímos o valor a variável.

print('Curso' in frase)  # True
print(frase.find('Curso'))  # 0
print(frase.find('vídeo'))  # -1
print(frase.lower().find('vídeo'))  # 9

dividido = frase.split()

print(dividido)  # ['Curso', 'em', 'Vídeo', 'Python']
print(dividido[0])  # Curso
print(dividido[2][3])  # e

print('-'.join(dividido))  # Curso-em-Vídeo-Python
