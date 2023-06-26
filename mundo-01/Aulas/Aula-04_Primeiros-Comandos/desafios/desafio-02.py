day = input("Em qual dia você nasceu? ")
month = input("Em que mês você nasceu? ")
year = input("Em que ano você ")
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m'
         }
print("Você nasceu no dia", cores['amarelo'], day, cores['limpa'], "de", cores['azul'], month, cores['limpa'], "de",
      cores['vermelho'], year, cores['limpa'], ". Correto?")
