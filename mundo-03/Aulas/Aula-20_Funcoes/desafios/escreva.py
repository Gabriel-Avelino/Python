def escreva(text):
    tamanho = int(len(text) + 4)
    print('~' * tamanho)
    print(text.center(tamanho))
    print('~' * tamanho)


escreva('Olá, mundo!')
escreva('Curso em Vídeo')
escreva('Python')
