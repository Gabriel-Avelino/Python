def parouimpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
if parouimpar(n):
    print('É par!')
else:
    print('Não é par!')
