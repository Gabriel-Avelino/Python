import os
import pygame

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m'
         }

pygame.init()

musica = input('\033[36mDigite o nome do arquivo de áudio: \033[m')
caminho = musica.replace(' ', '-')

print('Tocando "{}{}{}" usando player pygame'.format(cores['amarelo'], musica.title(), cores['limpa']))

# Obtenha o caminho absoluto do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Concatene o caminho absoluto com o nome do arquivo
caminho_arquivo = os.path.join(diretorio_atual, 'musicas-desafio21', '{}.mp3'.format(caminho))

pygame.mixer.music.load(caminho_arquivo)
pygame.mixer.music.play()
input()
pygame.event.wait()
