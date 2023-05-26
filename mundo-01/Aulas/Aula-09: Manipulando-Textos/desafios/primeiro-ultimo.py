nome = input('Digite seu nome completo: ').strip()
separado = nome.split()

print('Primeiro nome: {} \nÚltimo nome: {}'.format(separado[0], separado[-1]))
