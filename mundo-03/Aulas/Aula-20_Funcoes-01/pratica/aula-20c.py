def dobro(lst):
    for c, v in enumerate(lst):
        # value *= 2  # Não altera o valor
        lst[c] *= 2


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobro(valores)
print(valores)
