n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# print('A soma é {}, a subtração é {}, o produto é {}'.format(a, s, m))
# print('a divisão é {:.3f}, a divisão inteira é {} e a potência é {}'.format(d, di, e))  # Se quisermos, podemos limitar o número de casas decimais passando esse parâmetro nas chaves.

# Se não quisermos que a linha se quebre, basta colocar um end =''no final do primeiro print:
# print('A soma é {}, a subtração é {}, o produto é {}'.format(a, s, m), end=' ')  # Podemos também acrescentar caracteres que serão adicionados no final da linha através do end.
# print('a divisão é {:.3f}, a divisão inteira é {} e a potência é {}'.format(d, di, e))

# Agora, se quisermos que a linha da resposta se quebre, usamos \n:
print('A soma é {}, a subtração é {}, o produto é {}, \n a divisão é {:.3f}, a divisão inteira é {} e a potência é {}'.format(a, s, m, d, di, e))
