from datetime import datetime, timedelta

# hoje = datetime.now()
# um_dia = timedelta(days=1)

# amanha = hoje + um_dia
# ontem = hoje - um_dia
# print(ontem)

# prazo = datetime(2025, 7, 20)
# hoje = datetime.now()

# if hoje > prazo:
#     print("Prazo vencido!")
# else:
#     print("Ainda está no prazo.")

# agora = datetime.now()
# futuro = datetime(2025, 9, 23)
# dias_restantes = futuro - agora

# print(dias_restantes.days)

aniversario = datetime(2025, 7, 22)
hoje = datetime.now()

if aniversario.day == hoje.day and aniversario.month == hoje.month:
    print("Hoje é o dia do aniversário!")
elif aniversario > hoje:
    print("O aniversário ainda vai acontecer!")
elif aniversario < hoje:
    print("Já passou o aniversário!")