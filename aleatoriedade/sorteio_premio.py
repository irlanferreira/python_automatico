import random

convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

convidados_sorteados = random.sample(convidados, k=5)
premios_sorteados = random.sample(premios, k=5)

contador = 0
while contador < 5:
    convidado = convidados_sorteados[contador]
    premio = premios_sorteados[contador]
    print(f"O prêmio '{premio}' vai para '{convidado}' 🎉")
    contador+=1