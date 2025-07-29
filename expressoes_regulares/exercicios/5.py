import re
texto = "[INFO] Processo iniciado em 12:45\n[WARNING] Uso de memória alto às 13:05\n[ERROR] Falha crítica às 13:15"
expressao = r"\[(\w+)\].+(\d{2}:\d{2})"

resultados = re.findall(expressao, texto)
if resultados:
    for resultado in resultados:
        tipo = resultado[0]
        horario = resultado[1]
        print(f"Tipo de log: {tipo}\nHorário: {horario}\n")