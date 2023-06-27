expressao = str(input('Digite a expressão: ')).strip().replace('', ' ').split()
direito = expressao.count(')')
esquerdo = expressao.count('(')
total = esquerdo + direito

if total % 2 == 0 and esquerdo == direito:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
