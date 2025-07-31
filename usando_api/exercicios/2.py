import requests

resposta = requests.get("https://dog.ceo/api/breeds/image/random")

if resposta.status_code == 200:
    link = resposta.json()['message']
    print(f"Aqui sua imagem de cachorro: {link}")
else:
    print("Não foi possível processar sua solicitação.")