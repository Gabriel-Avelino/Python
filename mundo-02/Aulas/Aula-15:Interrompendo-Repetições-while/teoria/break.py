# As estruturas de repetição While podem ser interrompidas através do comando break, para utilizá-lo, a condição do nosso while deve ser igual a True:

while True:
    option = int(input('''Selecione uma opção:
[ 1 ] Dúvidas
[ 2 ] Reclamações
[ 3 ] Falar com um atendente
[ 4 ] Encerrar
Sua opção: '''))

    if option == 1:
        print('Qual sua dúvida?')
    elif option == 2:
        print('Qual sua reclamação?')
    elif option == 3:
        print('Encaminhando para um atendente')
        break
    elif option == 4:
        break
