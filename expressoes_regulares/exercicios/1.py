import re

texto = "Códigos disponíveis: ABC-1234, DEF-5678, GHI-0001, jkl-9999"
expressao = r"\w{3}-\d{4}"

resultados = re.findall(expressao, texto)

if resultados:
    print("Códigos encontrados:")
    for resultado in resultados:
        print(resultado)

