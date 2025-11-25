import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 5")
janela.geometry("400x300")

tk.Label(janela, text="Primeiro número: ").grid(row=0, column=0)
n1_entry = tk.Entry(janela)
n1_entry.grid(row=0, column=1)

tk.Label(janela, text="Primeiro número: ").grid(row=1, column=0)
n2_entry = tk.Entry(janela)
n2_entry.grid(row=1, column=1)

def somar():
    n1 = float(n1_entry.get())
    n2 = float(n2_entry.get())

    resposta_label['text'] = f"Resultado da soma: {n1 + n2}"


tk.Button(janela, text="Somar", command=somar).grid(row=2, columnspan=2)

resposta_label = tk.Label(janela, text="")
resposta_label.grid(row=3, columnspan=2)

janela.mainloop()