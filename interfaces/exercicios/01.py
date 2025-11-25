import tkinter as tk

nome = input("Digite seu nome: ")
janela = tk.Tk()
janela.geometry("400x300")

tk.Label(janela, text=f"Olá, {nome}").pack()

janela.mainloop()