# contador = 1

# while contador <= 5:
#     print(f"Contando: {contador}")
#     contador+=1

# senha = ''
# while senha != 'python':
#     senha = input(f"Digite sua senha: ")

# print("Senha correta!")

# for numero in range(6):
#     print(numero)

# frutas = ['maçã', 'melancia', 'uva', 'pêssego']
# for fruta in frutas:
#     print(f"Fruta atual: {fruta}")

# for multiplicador in range(1, 11):
#     for multiplicado in range(1, 11):
#         print(f"{multiplicado} x {multiplicador} = {multiplicado * multiplicador}")

# pessoas = ['ana', 'bruno', 'fernanda', 'daniel', 'felipe']
# for nome in pessoas:
#     print(f"Verificando: {nome}")
#     if nome == 'daniel':
#         print(f"Nome encontrado: {nome}")
#         break

# print("Busca encerrada")

for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(f"Número: {numero}")