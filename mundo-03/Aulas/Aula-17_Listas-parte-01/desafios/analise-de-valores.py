valores = []
c = 0

while True:
    numero = int(input('Digite um valor: '))

    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        continuar = ''
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in ['N', 'S']:
            break
    if continuar == 'N':
        break
print(f'''Foram digitados {len(valores)}''')
