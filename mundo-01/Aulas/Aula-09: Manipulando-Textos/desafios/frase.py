from unicodedata import normalize

frase = input('Digite uma frase: ').strip()
normalizada = normalize('NFD', frase).encode('ascii', 'ignore').decode('ascii')

print(normalizada)

print('''A frase digitada foi: {}
Quantas vezes aparece a letra A: {}
Em que posição ela aparece primeiro?: {}ª
Em que posição ela aparece pela última vez: {}ª
'''.format(frase, normalizada.upper().count('A'), normalizada.upper().find('A')+1, normalizada.upper().rfind('A')+1))
