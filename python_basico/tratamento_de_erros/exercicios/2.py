try:
    with open("relatorio2025.txt") as arquivo:
        print(arquivo.read())
except FileNotFoundError as erro:
    print(f"Arquivo não existe!")