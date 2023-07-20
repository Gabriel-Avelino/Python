from random import choice

first = input('Primeiro Aluno: ')
second = input('Segundo Aluno: ')
third = input('Terceiro Aluno: ')
fourth = input('Quarto Aluno: ')

print('O aluno escolhido foi {}'.format(choice([first, second, third, fourth])))
