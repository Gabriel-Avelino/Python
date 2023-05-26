from unicodedata import normalize

frase = input('Digite uma frase: ').strip()
normalizada = normalize('NFD', frase)

print('''A frase digitada foi: {}
Quantas vezes aparece a letra A: {}
Em que posição ela aparece primeiro?: {}
Em que posição ela aparece pela última vez: {}
'''.format(frase, normalizada.upper().count('A'), normalizada.upper().find('A'), normalizada.upper().rfind('A')))
