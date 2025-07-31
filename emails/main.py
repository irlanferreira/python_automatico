import smtplib
from email.message import EmailMessage

meu_email = "cursopythonautomatico@gmail.com"
senha = "rvyo jzbl edty mkxu"
destinatario = "cursopythonautomatico@gmail.com"

msg = EmailMessage()
msg['From'] = meu_email
msg['Subject'] = "Teste"
msg['To'] = destinatario
msg.add_alternative("<h1>Olá!</h1>", subtype="html")

with open('gato.png', 'rb') as arquivo:
    conteudo_arquivo = arquivo.read()
    nome_arquivo = arquivo.name
    msg.add_attachment(conteudo_arquivo, maintype="image", subtype="png", filename=nome_arquivo)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(meu_email, senha)
    smtp.send_message(msg)