with open("acesso.log", encoding="utf-8") as arquivo:
    palavra_chave = input("Qual palavra quer usar?: ")
    for linha in arquivo.readlines():
        if palavra_chave.upper() in linha:
            print(linha)