import smtplib
from email.message import EmailMessage
from openpyxl import Workbook

vendas = [
        {'produto': 'Teclado', 'qtd': 3, 'valor': 150.00},
        {'produto': 'Mouse', 'qtd': 5, 'valor': 80.00},
        {'produto': 'Monitor', 'qtd': 2, 'valor': 900.00},
        {'produto': 'Headset', 'qtd': 4, 'valor': 250.00},
        {'produto': 'Webcam', 'qtd': 1, 'valor': 400.00}
    ]

def gerar_planilha(vendas):
    arquivo_vendas = Workbook()
    planilha_vendas = arquivo_vendas.active
    planilha_vendas.title = "Vendas"
    planilha_vendas.append(['Produto', 'Valor', 'Quantidade'])
    for produto in vendas:
        planilha_vendas.append([produto['produto'], produto['valor'], produto['qtd']])
    arquivo_vendas.save('relatorio_vendas.xlsx')

def enviar_relatorio():
    meu_email = "cursopythonautomatico@gmail.com"
    senha = "rvyo jzbl edty mkxu"
    destinatario = meu_email

    gerar_planilha(vendas)

    msg = EmailMessage()
    msg['From'] = meu_email
    msg['Subject'] = "Relatório de Vendas gerado automaticamente"
    msg['To'] = destinatario
    msg.set_content("Segue em anexo o relatório de vendas gerado em python.")

    with open('relatorio_vendas.xlsx', 'rb') as arquivo:
        conteudo = arquivo.read()
        nome_arquivo = arquivo.name
        msg.add_attachment(conteudo, maintype="application", subtype="xlsx", filename=nome_arquivo)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(meu_email, senha)
        smtp.send_message(msg)


enviar_relatorio()