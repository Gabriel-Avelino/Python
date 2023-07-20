palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for l in p:
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
            print(l, end=' ')

