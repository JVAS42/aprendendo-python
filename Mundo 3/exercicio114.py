import requests

def verifica_site(url):
    try:
        site = requests.get(url, timeout=1)
    except requests.exceptions.RequestException:
        print(f'O site {url} não está acessível! 🚫')
    else:
        print(f'O site {url} está acessível! ✅')


verifica_site('https://www.pudim.com.br/')
