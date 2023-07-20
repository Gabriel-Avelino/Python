import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatar(p)} é {moeda.formatar(moeda.metade(p))}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.formatar(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.formatar(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {moeda.formatar(moeda.diminuir(p, 13))}')
