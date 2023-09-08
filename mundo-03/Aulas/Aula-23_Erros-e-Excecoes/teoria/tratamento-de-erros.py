# Para fazer tratamento de erros usamos a seguinte estrutura:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    result = a / b
except:
    print('Erro!')  # É possível ter vários except e mostrar os erros através da classe Exception.
    # Também é possível usar mensagens personalizadas
else:
    print(result)
finally:
    print('Volte sempre!')
