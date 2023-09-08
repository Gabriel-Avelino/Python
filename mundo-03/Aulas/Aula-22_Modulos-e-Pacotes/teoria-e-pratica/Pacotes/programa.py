# Quando os módulos se tornam muito grandes, podemos utilizar os pacotes, pastas que reúnem vários códigos.
# Para criar um pacote, basta criar uma estrutura de pastas, onde em cada uma delas haverá um arquivo 'ini.py'.
# Esse arquivo irá conter nossas funções:

from uteis import numbers

num = int(input('Digite um valor: '))
fat = numbers.fatorial(num)
print(f'O fatorial de {num} é {fat}')