from random import shuffle

first = str(input('Primeiro Aluno: '))
second = str(input('Segundo Aluno: '))
third = str(input('Terceiro Aluno: '))
fourth = str(input('Quarto Aluno: '))
ordem = [first, second, third, fourth]
shuffle(ordem)

print('Os alunos apresentarão na seguinte ordem: {}'.format(ordem))
