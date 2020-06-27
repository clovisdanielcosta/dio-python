# Antes de usar o requests precisa instalar pelo 'pip install requests'
import requests

# Consumindo api da Braziliex de criptomoedas
def retorna_braziliex(coin):
    response = requests.get('https://braziliex.com/api/v1/public/ticker/{}'.format(coin))
    dados_coin = response.json()
    print(dados_coin)
    print(dados_coin['last'])

if __name__ == '__main__':
    retorna_braziliex('eth_btc')
    retorna_braziliex('eth_brl')
    retorna_braziliex('ltc_btc')
    retorna_braziliex('btc_brl')

