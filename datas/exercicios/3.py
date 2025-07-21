from datetime import datetime

def gerar_assinatura(nome):
    agora = datetime.now()
    print(agora.strftime(f"Assinatura gerada por {nome} em %d/%m/%Y às %H:%M"))

nome = input("Digite seu nome: ")
gerar_assinatura(nome)