from datetime import datetime

with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Estou aprendendo python!\n")
    agora = datetime.now()
    arquivo.write(agora.strftime("%d/%m/%Y %H:%M"))