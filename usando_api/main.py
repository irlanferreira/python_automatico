import requests

# cep = "01001000"

# url = f"https://viacep.com.br/ws/{cep}/json"

# resposta = requests.get(url)
# if resposta.status_code == 200:
#     print(resposta.json())
# else:
#     print(resposta.status_code)

resposta = requests.get("https://api.thecatapi.com/v1/images/search")
if resposta.status_code == 200:
    gato_url = resposta.json()[0]['url']
    print(f"Aqui sua foto de gato: {gato_url}")