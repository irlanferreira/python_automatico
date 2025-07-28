import re
texto = "Obrigado @joaopereira e @maria_silva pela ajuda! Também cito @123julio e @_admin"
expressao = r"@\w+"

resultados = re.findall(expressao, texto)

if resultados:
    print("Usuários encontrados:")
    for resultado in resultados:
        print(resultado)