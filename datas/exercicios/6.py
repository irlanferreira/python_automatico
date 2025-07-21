from datetime import datetime, timedelta

data_fabricacao = input("Digite a data de fabricação do produto: ")
data_fabricacao = datetime.strptime(data_fabricacao, "%d/%m/%Y")
data_vencimento = data_fabricacao + timedelta(days=180)
hoje = datetime.now()

print(data_vencimento.strftime("A data de vencimento é dia %d/%m/%Y"))

if hoje.date() == data_vencimento.date():
    print("O produto vence hoje!")
elif hoje > data_vencimento:
    print("O produto já venceu!")
elif hoje < data_vencimento:
    print("O produto ainda vai vencer!")
