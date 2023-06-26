name = input("Qual seu nome? ")
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m'
         }
print("Bem-vindo", cores['pretoebranco'], name, cores['limpa'], "! Prazer em te conhecer!")