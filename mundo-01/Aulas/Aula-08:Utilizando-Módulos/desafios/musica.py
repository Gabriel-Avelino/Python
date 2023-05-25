import os
os.chdir("musicas-desafio21")
file = input("Digite a música que você deseja tocar: ")

print('Tocando "{}" usando player nativo'.format(file))
os.system("afplay " + file)
