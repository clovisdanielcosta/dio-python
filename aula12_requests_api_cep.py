# Antes de usar o requests precisa instalar pelo 'pip install requests'
import requests

def retorna_cep(cep):

    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code) # Verifica se ocorreu tudo bem '200'
    print(response.json()) # Transforma resultado numa string
    dados_cep = response.json() # Armazena resultado numa variável lista de strings
    print(dados_cep['logradouro']) # Trabalha com os elementos da lista

    return dados_cep

if __name__ == '__main__':
    retorna_cep('81050390')
