import qrcode

redes_sociais = {
    "Youtube":"https://youtube.com/@lan_code",
    "Udemy":"https://www.udemy.com/user/irlan-ferreira-da-silva-2/",
    "Linkedin":"https://www.linkedin.com/in/irlan-ferreira-b66b80263/"
}
for chave, valor in redes_sociais.items():
    img = qrcode.make(valor)
    img.save(f"qrcodes/{chave}.png")