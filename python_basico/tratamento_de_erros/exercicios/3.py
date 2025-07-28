lista = ["Python", "Excel", "API"]
try:
    indice = int(input("Digite um índice para acessar um valor: "))
    print(lista[indice])
except ValueError as erro:
    print(f"Valor inválido!")
except IndexError as erro:
    print("Índice inválido!")