import re

texto = "Os carros estacionados são: KDA-2341, JHU-8877 e MNO-0000"
expressao = r"\w{3}-\d{4}"

novo_texto = re.sub(expressao, "PLACA", texto)

print(novo_texto)