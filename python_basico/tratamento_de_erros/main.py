try:
    int("oi")
except ValueError as erro:
    print("Erro de valor!")
except ZeroDivisionError as error:
    print("Erro de divisão!")

print("Codigo rodando normalmente")

