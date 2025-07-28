try:
    numero = int(input("Digite um número: "))
except Exception as erro:
    print(f"Valor inválido: {erro}")