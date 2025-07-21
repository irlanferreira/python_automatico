# def saudacao():
#     print("Olá, Seja bem vindo!")

# def saudacao(nome):
#     print(f"Olá, {nome}! Seja bem vindo!")

# saudacao("Lan")

# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     print(f"O resultado da soma entre {numero1} e {numero2} é {resultado}")

# somar(6, 8)

# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     return resultado

# print(somar(5, 5))

def calcular_descontos(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final

print(calcular_descontos(200, 100))