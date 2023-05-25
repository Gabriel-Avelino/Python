import os
import pygame

pygame.init()

musica = input('Digite o nome do arquivo de áudio: ')

print('Tocando "{}" usando player pygame'.format(musica))

# Obtenha o caminho absoluto do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Concatene o caminho absoluto com o nome do arquivo
caminho_arquivo = os.path.join(diretorio_atual,'musicas-desafio21', '{}.mp3'.format(musica))

pygame.mixer.music.load(caminho_arquivo)
pygame.mixer.music.play()
input()
pygame.event.wait()
