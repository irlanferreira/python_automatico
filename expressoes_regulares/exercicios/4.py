import re
texto = "Veículos: CAR-2023, MOTO-2018, BUS-2015"
expressao = r"(\w+)-(\d{4})"

resultados = re.findall(expressao, texto)
if resultados:
    for resultado in resultados:
        print(f"Tipo de veículo: {resultado[0]}\nAno: {resultado[1]}\n")