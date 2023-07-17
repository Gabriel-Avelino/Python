# Também é possível criar funções que receberão quantidades indefinidas de parâmetros:
def contador(*num):
    print(num)  # Resulta em uma tupla.


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
