def moeda(value=0.0, moeda='R$'):
    return f'{moeda}{value:.2f}'.replace('.', ',')

