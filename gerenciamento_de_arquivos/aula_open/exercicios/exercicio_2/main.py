frase = input("Digite uma frase: ")

with open("mensagem.txt","w", encoding='utf-8') as arquivo:
    arquivo.write(frase)

    print(f"A frase tem {len(frase)} letras.")