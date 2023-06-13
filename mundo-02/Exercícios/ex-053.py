from unidecode import unidecode
frase = str(input('Digite uma frase: ')).strip()

comparativo = unidecode(frase.replace(' ', '')).upper()
inverso = ''.join(reversed(comparativo))

if comparativo == inverso:
    print('''O inverso de {} é {}
Temos um palíndromo!'''.format(comparativo, inverso))
else:
    print('''O inverso de {} é {}
A frase digitada não é um palíndromo!'''.format(comparativo, inverso))
