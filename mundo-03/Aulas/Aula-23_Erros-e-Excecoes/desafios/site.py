import requests
try:
    resp = requests.get('http://www.pudim.com.br')
except:
        print(f'\033[31mO site pudim não está acessível no momento.\033[m')
else:
    print(f'\033[32mConsegui acessar o site pudim com sucesso!\033[m')