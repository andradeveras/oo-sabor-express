import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #Endpoint 

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    print(dados_json)
else:
    print(f"o erro foi {response.status_code}")