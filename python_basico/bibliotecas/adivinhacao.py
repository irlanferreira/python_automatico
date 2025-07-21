from random import randint

tentativas = 1
numero_aleatorio = randint(1, 10)
while True:
    numero_digitado = int(input("Digite um número: "))
    if numero_digitado == numero_aleatorio:
        print(f"Parabéns! Você acertou o número!\nTentativas: {tentativas}")
        break
    tentativas+=1
    if numero_digitado > numero_aleatorio:
        print("Muito alto!")
    if numero_digitado < numero_aleatorio:
        print("Muito baixo!")