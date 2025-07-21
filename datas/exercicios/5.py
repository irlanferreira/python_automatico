from datetime import datetime, timedelta

evento_data = input("Digite a data do evento (ex: d/m/y): ")
evento_data = datetime.strptime(evento_data, "%d/%m/%Y")
hoje = datetime.now()

if hoje.date() == evento_data.date():
    print("O evento é hoje!")
elif hoje > evento_data:
    print("Já passou do evento.")
elif hoje < evento_data:
    print("O evento ainda vai acontecer.")
