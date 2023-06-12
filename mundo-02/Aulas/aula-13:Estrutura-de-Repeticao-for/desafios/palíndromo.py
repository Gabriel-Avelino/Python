from unidecode import unidecode
frase = str(input('Digite uma frase: ')).strip()
fraseUnida = unidecode(frase.replace(" ", "")).upper()
inverso = "".join(reversed(fraseUnida))
palindromo = []

for c in range(0, len(inverso)):
    if fraseUnida[c] == inverso[c]:
        palindromo.append('true')
    else:
        palindromo.append('false')

if 'false' in palindromo:
    print('A frase "{}" NÃO É um palíndromo'.format(frase))
else:
    print('A frase "{}" É um palíndromo'.format(frase))
