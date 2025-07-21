from datetime import datetime

data_atual = datetime.now()
hora = 2

if hora < 12 and hora > 3:
    print("Bom dia!")
elif hora > 12 and hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")

print(f"Agora são {hora} horas.")