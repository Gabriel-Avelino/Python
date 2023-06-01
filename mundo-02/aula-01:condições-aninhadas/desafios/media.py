media = float(input('Digite a primeira nota do aluno: '))
media += float(input('Digite a segunda nota do aluno: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'
         }

media /= 2

if media < 5:
    print('{1}Sua média foi: {0}.{2} Você foi REPROVADO!{3}'.format(media, cores['azul'], cores['vermelho'], cores['limpa']))
elif media == 5 and media < 6.9:
    print('{1}Sua média foi: {0}.{2} Você está de RECUPERAÇÃO!{3}'.format(media, cores['azul'], cores['amarelo'], cores['limpa']))
else:
    print('{1}Sua média foi: {0}.{2} Você foi APROVADO!{3}'.format(media, cores['azul'], cores['verde'], cores['limpa']))
