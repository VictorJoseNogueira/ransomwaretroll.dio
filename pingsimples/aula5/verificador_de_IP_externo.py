import re
import json
from urllib.request import urlopen


URL = 'https://ipinfo.io/json'
resposta = urlopen(URL)
dados = json.load(resposta)
IP = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('detalhes de IP externo\n')
print(f'IP: {IP}\nregiao: {regiao}\npais: {pais}\ncidade: {cidade}\norganização: {org}')
