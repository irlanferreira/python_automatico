from modulos import matematica, mensagens, formatador, usuario

# nome = input("Digite seu nome: ")
# numero = float(input("Digite um número: "))

# mensagens.boas_vindas(nome)
# print(f"O dobro de {numero} é {matematica.dobro(numero)}.")
# print(f"A metade de {numero} é {matematica.metade(numero)}.")

# frase = input("Digite uma frase: ")
# print(formatador.caixa_alta(frase))

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if usuario.validar_idade(idade):
    perfil_usuario = usuario.criar_perfil(nome, idade)
    print("Perfil criado!")
else:
    print("Você não tem idade minima para entrar.")