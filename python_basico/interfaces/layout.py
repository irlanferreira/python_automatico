import tkinter as tk

janela = tk.Tk()
janela.title("Posicinamento")
janela.geometry("400x300")

tk.Label(janela, text="Digite seu nome").grid(row=0, column=0)
nome_entry = tk.Entry(janela)
nome_entry.grid(row=0, column=1)

tk.Label(janela, text="Digite sua idade").grid(row=1, column=0)
idade_entry = tk.Entry(janela)
idade_entry.grid(row=1, column=1)

def enviar():
    nome = nome_entry.get()
    idade = idade_entry.get()

    resposta_label['text'] = f"Prazer, {nome}. Você tem {idade} anos."

tk.Button(janela, text="Enviar", command=enviar).grid(row=2, columnspan=2)
resposta_label = tk.Label(janela, text="")
resposta_label.grid(row=3, columnspan=2)

janela.mainloop()