primeiro = int(input('1º Termo: '))
razao = int(input('Razão: '))
c = 1

while c < 11:
    result = primeiro + (c - 1) * razao
    print(result)
    c += 1
print('FIM')
