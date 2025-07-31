import requests

valor_real = float(input("Digite um valor em R$: "))

resultado = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
if resultado.status_code == 200:
    dolar = float(resultado.json()['USDBRL']['bid'])
    valor_dolar = valor_real / dolar
    print(f"O valor digitado em dólar é {valor_dolar:.2f}")
else:
    print("Não foi possível concluir sua solicitação.")