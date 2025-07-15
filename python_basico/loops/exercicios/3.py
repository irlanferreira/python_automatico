total = 0
while True:
    valor = float(input("Insira algo no cofrinho: "))
    if valor == 0:
        break
    total += valor

print(f"O valor total guardado é: {total}")