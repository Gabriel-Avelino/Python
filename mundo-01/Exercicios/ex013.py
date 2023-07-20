salario = float(input('Qual é o salário do funcionário?: R$'))
aumento = float(input('Qual a porcentagem do aumento salarial?: '))

print('Com o aumento salarial de {}%, o salário do funcionário, que atualmente é de R${:.2f} passará para R${:.2f}'.format(aumento, salario, (salario + (salario * aumento / 100))))
