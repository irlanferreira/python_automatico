import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Minha Janelinha")
janela.geometry("400x300")

mensagem = tk.Label(janela, text="Meu primeiro label")
mensagem.pack()

def resposta_botao():
    nome = nome_entry.get()
    if not nome:
        messagebox.showerror("ERRO", "Você não digitou seu nome.")
        return
    
    mensagem['text'] = f"Olá, {nome}!"
    messagebox.showinfo("Alerta", "Programa executado com sucesso.")

nome_entry = tk.Entry(janela)
nome_entry.pack()

tk.Button(janela, text="Botãozinho", command=resposta_botao).pack()

janela.mainloop()