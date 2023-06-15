from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = ''

while opcao != '5':
    opcao = str(input('''    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa
>>>>> Qual é a sua opção? ''')).strip().upper()
    if opcao == '1' or opcao == 'SOMAR':
        opcao = '1'
        result = valor1 + valor2
        print('A soma entre {} + {} é {}'.format(valor1, valor2, result))
    elif opcao == '2' or opcao == 'MULTIPLICAR':
        opcao = '2'
        result = valor1 * valor2
        print('O resultado de {} x {} é {}'.format(valor1, valor2, result))
    elif opcao == '3' or opcao == 'MAIOR':
        opcao = '3'
        if valor1 != valor2:
            if valor1 > valor2:
                maior = valor1
            else:
                maior = valor2
            print('Entre {} e {} o maior valor é {}'.format(valor1, valor2, maior))
        else:
            print('Os dois valores são iguais')
    elif opcao == '4' or opcao == 'NOVOS NÚMEROS':
        opcao = '4'
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == '5' or opcao == 'SAIR DO PROGRAMA':
        opcao = '5'
        print('Finalizando...')
    else:
        opcao = ''
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
