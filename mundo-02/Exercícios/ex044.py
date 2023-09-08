print('{:=^40}'.format(' LOJAS AVELINO '))
preco = float(input('\033[33mPreço das compras:  \033[32mR$'))
pagamento = str(input('''\033[31mFORMAS DE PAGAMENTO
\033[34m[ 1 ] \033[37mà vista dinheiro/cheque
\033[34m[ 2 ] \033[37mà vista no cartão
\033[34m[ 3 ] \033[37m2x no cartão
\033[34m[ 4 ] \033[37m3x ou mais no cartão
\033[35mQual é a opção? ''')).upper()

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
if pagamento == '1' or pagamento == 'À VISTA DINHEIRO/CHEQUE' or pagamento == '2' or pagamento == 'À VISTA NO CARTÃO' or pagamento == '3' or pagamento == '2X NO CARTÃO' or pagamento == '4' or pagamento == '3X OU MAIS NO CARTÃO':
    if pagamento == '1' or pagamento == 'À VISTA DINHEIRO/CHEQUE':
        final = preco - preco * 10/100
        msg = '{2}Sua compra de {3}R${0:.2f}{2} vai custar {4}R${1:.2f}{2} no final.'.format(preco, final, cores['cinza'], cores['vermelho'], cores['verde'])
    elif pagamento == '2' or pagamento == 'À VISTA NO CARTÃO':
        final = preco - preco * 5/100
        msg = '{2}Sua compra de {3}R${0:.2f}{2} vai custar {4}R${1:.2f}{2} no final.'.format(preco, final, cores['cinza'], cores['vermelho'], cores['verde'])
    elif pagamento == '3' or pagamento == '2X NO CARTÃO':
        final = preco
        parcela = final / 2
        print('{1}Sua compra será parcelada em {2}2x{1} de {3}R${0:.2f} SEM JUROS'.format(parcela, cores['ciano'], cores['amarelo'], cores['verde']))
        msg = '{2}Sua compra de {3}R${0:.2f}{2} vai custar {4}R${1:.2f}{2} no final.'.format(preco, final, cores['cinza'], cores['vermelho'], cores['verde'])
    elif pagamento == '4' or pagamento == '3X OU MAIS NO CARTÃO':
        quantidadeParcelas = int(input('\033[31mQuantas parcelas? '))
        if quantidadeParcelas >= 3:
            final = preco + preco * 20 / 100
            parcela = final / quantidadeParcelas
            print('{2}Sua compra será parcelada em {3}{0}x{2} de {4}R${1:.2f} COM JUROS'.format(quantidadeParcelas, parcela, cores['ciano'], cores['amarelo'], cores['vermelho']))
            msg = '{2}Sua compra de {3}R${0:.2f}{2} vai custar {4}R${1:.2f}{2} no final.'.format(preco, final, cores['cinza'], cores['vermelho'], cores['verde'])
        else:
            msg = '{}Quantidade de parcelas inválida. Aceitamos somente 3 ou mais parcelas nessa opção.'.format(cores['vermelho'])
    print(msg)
else:
    print('Opção Inválida')
