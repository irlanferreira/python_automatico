from datetime import datetime, timedelta

hoje = datetime.now()
fim_do_ano = datetime(hoje.year, 12, 31)

dias_restantes = fim_do_ano - hoje
dias_restantes = dias_restantes.days

print(f"Faltam {dias_restantes} dias para o dia 31 de dezembro.")