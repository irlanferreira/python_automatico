import requests

nome = input("Digite seu nome: ")
api_url = f"https://api.agify.io/?name={nome}"

resposta = requests.get(api_url)
if resposta.status_code == 200:
    idade_media = resposta.json()['age']
    print(f"A idade média do nome {nome} é {idade_media}")
else:
    print("Não foi possível concluir sua solicitação.")