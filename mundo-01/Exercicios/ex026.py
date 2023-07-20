from unidecode import unidecode

frase = str(input('Digite uma frase: ')).strip()
# normalizada = normalize('NFD', frase.upper()).encode('ascii', 'ignore').decode('ascii')
normalizada = unidecode(frase).upper()
print('A letra A apareceu {} vezes na frase \nA primeira letra A apareceu na posição {} \nA última letra A apareceu na posição {}'.format(normalizada.count('A'), normalizada.find('A') + 1, normalizada.rfind('A') + 1))
