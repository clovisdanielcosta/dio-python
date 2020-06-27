# Antes de usar o requests precisa instalar pelo 'pip install requests'
import requests

# Fazendo requisição de um site para estudar ou pegar dados
def retorna_site(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_site('https://braziliex.com/')
    print(response)