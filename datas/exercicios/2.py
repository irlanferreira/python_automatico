from datetime import datetime

agora = datetime.now()
mes_atual = agora.month

print(f"Hoje é o {mes_atual}° mês do ano. Faltam {13 - mes_atual} mêses para o ano acabar.")