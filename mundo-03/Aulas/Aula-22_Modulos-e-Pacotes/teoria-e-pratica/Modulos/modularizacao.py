# Surgiu na década de 80 com o objetivo de dividir um programa grande.
# Esse processo aumenta a legibilidade e facilita a manutenção.
# Para fazer isso, basta criar um arquivo a parte e importa-lo da seguinte forma:
from operations import *


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
