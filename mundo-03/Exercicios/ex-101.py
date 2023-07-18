def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
resp = int(input('Em que ano você nasceu? '))
print(voto(resp))
