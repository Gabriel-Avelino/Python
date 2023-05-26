nome = input('Digite seu nome completo: ').strip()

print('''Nome: {} 
Nome em letras maiúsculas: {} 
Nome em letras minúsculas: {} 
Quantidade de letras: {} 
Quantidade de letras do primeiro nome: {}'''.format(nome, nome.upper(), nome.lower(), len(nome.replace(' ', '')), len(nome.split()[0])))
