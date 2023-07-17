palavras = (
'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
'programador', 'futuro')
for pos, p in enumerate(palavras):
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    c = 0
    while c < len(p):
        if p[c] == 'a' or p[c] == 'e' or p[c] == 'i' or p[c] == 'o' or p[c] == 'u':
            print(p[c], end=' ')
        c += 1
