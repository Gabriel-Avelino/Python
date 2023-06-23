nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    pos = int(input('Digite um número entre 0 e 20: '))
    if pos > 20 or pos < 0:
        print('Tente novamente.', end=' ')
    else:
        print(f'Você digitou o número {nums[pos]}')
        continuar = ''
        while continuar not in ('S', 'N'):
            continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
print('=' * 35)
print('PROGRAMA FINALIZADO! Volte sempre!')

