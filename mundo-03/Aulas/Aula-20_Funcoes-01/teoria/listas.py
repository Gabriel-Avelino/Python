# Também é possível trabalhar funções usando listas:
def dobra(lst):
    for c, v in enumerate(lst):
        lst[c] *= 2


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
