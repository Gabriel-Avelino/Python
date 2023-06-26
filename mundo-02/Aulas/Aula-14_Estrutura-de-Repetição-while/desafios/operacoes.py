from time import sleep

carregando = ''
opcao = ''
resultado = 0

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))

while opcao != '5':
    opcao = str(input('''Escolha uma opção: 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Sua Opção: ''')).lower().strip()

    if opcao == '1' or opcao == 'somar':
        resultado = num1 + num2
        print('Soma = {}'.format(resultado))
    elif opcao == '2' or opcao == 'multiplicar':
        opcao = '2'
        resultado = num1 * num2
        print('Multiplicar = {}'.format(resultado))
    elif opcao == '3' or opcao == 'maior':
        opcao = '3'
        if num1 > num2:
            print('O número {} é o maior'.format(num1))
        elif num1 == num2:
            print('Os dois números são iguais')
        else:
            print('O número {} é o maior'.format(num2))
    elif opcao == '4' or opcao == 'novos números':
        opcao = '4'
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: '))
    elif opcao == '5' or opcao == 'sair do programa':
        opcao = '5'
        print('FINALIZANDO PROGRAMA')
        sleep(2)
print('\nPROGRAMA FINALIZADO')
