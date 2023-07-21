import requests
try:
    resp = requests.get('http://www.pudim.com.br')
    if resp.status_code == 200:
        print(f'\033[32mConsegui acessar o site pudim com sucesso!\033[m')
except:
        print(f'\033[31mO site pudim não está acessível no momento.\033[m')