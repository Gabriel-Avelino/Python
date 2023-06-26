from math import sqrt, floor  # Se quisermos usar mais de uma funcionalidade, basta importá-la usando uma vírgula
num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a: {:.2f}'.format(num, floor(raiz)))

# Obs: Para visualizar as bibliotecas disponíveis, é preciso acessar a documentação do Python através do site: python.org
