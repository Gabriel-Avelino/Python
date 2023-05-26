# As funcionalidades de divisão permitem dividir strings
frase = 'Curso em Vídeo Python'
separado = frase.split()

print(separado)  # Divide a string se baseando nos espaços e adiciona os pedaços em uma lista.

# De forma análoga a esse comando, há o join que une a string novamente
junto = '-'.join(separado)

print(junto)
