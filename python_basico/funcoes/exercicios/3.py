def par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero_usuario = float(input("Digite um número: "))
print(f"O número {numero_usuario} é {par_impar(numero_usuario)}")