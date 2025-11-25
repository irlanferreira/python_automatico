import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 2")
janela.geometry("400x300")

tk.Label(janela, text="Digite um número").pack()
numero_entry = tk.Entry(janela)
numero_entry.pack()

def calcular_dobro():
    numero = float(numero_entry.get())
    resposta['text'] = numero * 2

tk.Button(janela, text="Calcular dobro", command=calcular_dobro).pack()
resposta = tk.Label(janela, text="")
resposta.pack()

janela.mainloop()