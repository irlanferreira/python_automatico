usuario = {
    'nome': input("Digite seu nome: "),
    'idade': int(input("Digite sua idade: "))
}

if usuario['idade'] >= 18:
    print("Acesso liberado!")
else:
    print("Acesso negado!")