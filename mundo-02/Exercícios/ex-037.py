num = int(input('\033[33mDigite um número inteiro: '))
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

base = str(input('''\033[35mEscolha uma das bases para conversão: 
\033[34m[ 1 ] \033[37mConverter para \033[32mBINÁRIO
\033[34m[ 2 ] \033[37mConverter para \033[36mOCTAL
\033[34m[ 3 ] \033[37mConverter para \033[31mHEXADECIMAL
\033[37mSua opção: ''')).upper()

if base == '1' or base == 'BINÁRIO' or base == 'CONVERTER PARA BINÁRIO' or base == '2' or base == 'OCTAL' or base == 'CONVERTER PARA OCTAL' or base == '3' or base == 'HEXADECIMAL' or base == 'CONVERTER PARA HEXADECIMAL':
    if base == '1' or base == 'BINÁRIO' or base == 'CONVERTER PARA BINÁRIO':
        base = 'BINÁRIO'
        convertido = bin(num)
        resultcor = cores['verde']
    elif base == '2' or base == 'OCTAL' or base == 'CONVERTER PARA OCTAL':
        base = 'OCTAL'
        convertido = oct(num)
        resultcor = cores['ciano']
    else:
        base = 'HEXADECIMAL'
        convertido = hex(num)
        resultcor = cores['vermelho']
    print('{3}{0}{4} convertido para {5}{1}{4} é igual a {5}{2}'.format(num, base, convertido[2:], cores['amarelo'], cores['violeta'], resultcor))
else:
    print('{}Opção inválida. Tente novamente.'.format(cores['vermelho']))
