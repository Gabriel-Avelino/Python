nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

opcao = int(input('Digite um número entre 0 e 20: '))

while opcao >= len(nums) or opcao < 0:
    opcao = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {nums[opcao]}')
