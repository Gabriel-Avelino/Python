nota1 = float(input('\033[36mPrimeira Nota: '))
nota2 = float(input('\033[36mSegunda Nota: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m',
         'violeta': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'azul-claro': '\033[96m',
         'verde-claro': '\092[32m'
         }
media = (nota1 + nota2)/2

if media < 5:
    resultado= '\033[91mREPROVADO'
elif 5 <= media < 7:
    resultado = '\033[93mem RECUPERAÇÃO'
else:
    resultado = '\033[92mAPROVADO'

print('''{4}Tirando {5}{0}{4} e {5}{1}{4}, a média do aluno é {6}{2}{7}
O aluno está {3}'''.format(nota1, nota2, media, resultado, cores['violeta'], cores['cinza'], cores['azul'], cores['azul-claro']))
