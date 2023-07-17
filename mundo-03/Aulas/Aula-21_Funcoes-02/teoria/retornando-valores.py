# Também é possível criar funções que retornam valores. Para retornar um valor basta usar o "return":
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


# Depois é possível salvar os retornos dentro de variáveis:
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
