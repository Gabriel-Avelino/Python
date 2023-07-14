def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


print(f'{"Controle de Terrenos"}')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
