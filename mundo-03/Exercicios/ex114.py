import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'\033[31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site pudim com sucesso!\033[m')
    for l in site.readlines():
        print(l)
