firstNumber = input("Digite um número: ")
secondNumber = input("Digite outro número: ")
result = firstNumber + secondNumber
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m',
         'verde': '\033[32m'
         }

print("A soma dos dois números é: ", cores['verde'], result, cores['limpa'])
