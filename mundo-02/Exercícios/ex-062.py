print('{:^20}'.format('Gerador de PA'))
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão  da PA: '))

termos = 11
novosTermos = ''
c = 1


while novosTermos != 0:
    while c < termos:
        enesimo = primeiro + (c - 1) * razao
        print(enesimo, end=' → ')
        c += 1
    print('PAUSA')
    novosTermos = int(input('Quantos termos você quer mostrar a mais? '))
    termos += novosTermos
print('Progressão finalizada com {} termos mostrados.'.format(c - 1))
