nome = str(input('Digite seu nome completo: ')).strip()

print('''Analisando seu nome...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é: {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras 
'''.format(nome.upper(), nome.lower(), len(nome.replace(' ', '')), nome.split()[0], len(nome.split()[0])))
