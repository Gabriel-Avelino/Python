def leianumero(msg):
    while True:
        preco = str(input(msg)).strip()
        precolimpo = preco.replace(',', '').replace('.', '')
        if precolimpo.isdigit():
            if ',' in preco:
                preco = preco.replace(',', '.')
            preco = float(preco)
            return preco
        else:
            print(f'\033[31mERRO: \"{preco}\" é um preço inválido!\033[m"')
