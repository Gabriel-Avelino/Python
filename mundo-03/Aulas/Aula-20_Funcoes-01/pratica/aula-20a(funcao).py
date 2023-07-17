def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print()


# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
# Soma(4)  # Dá erro por estar passando somente um parâmetro.
soma(4, 1)
# Soma(3, 4, 5)  # Dá erro, há somente dois parâmetros.

# Também posso especificar qual valor pertence a qual parâmetro:
soma(a=3, b=6)
soma(b=3, a=6)

# soma(b=3, 6)  # Gera erro, se for explicitar, explicite os dois.
