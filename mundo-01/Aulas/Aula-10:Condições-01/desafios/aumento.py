salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250:
    print('Esse funcionário recebe R${:.2f}. Logo, seu novo salário será de R$ {:.2f}'.format(salario, (salario + (salario * (10 / 100)))))
else:
    print('Esse funcionário recebe R${:.2f}. Logo, seu novo salário será de R$ {:.2f}'.format(salario, (salario + (salario * (15 / 100)))))
