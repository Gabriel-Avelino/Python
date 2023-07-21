def leianumero(msg):
    while True:
        preco = str(input(msg)).strip()
        if ',' in preco:
            preco = preco.replace(',', '.')
        if preco.isdigit():
            preco = float(preco)
            return preco
        else:
            print(f'\033[31mERRO: \"{preco}\" é um preço inválido!\033[m"')
