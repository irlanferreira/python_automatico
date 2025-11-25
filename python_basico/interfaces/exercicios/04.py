import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 4")
janela.geometry("400x300")

frase_entry = tk.Entry(janela)
frase_entry.pack()

def maiusculas():
    resultado_label['text'] = frase_entry.get().upper()

def minusculas():
    resultado_label['text'] = frase_entry.get().lower()

tk.Button(janela, text="Maiúsculas", command=maiusculas).pack()
tk.Button(janela, text="Minúsculas", command=minusculas).pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

def limpar():
    resultado_label["text"] = ""

tk.Button(janela, text="Limpar", command=limpar).pack()

janela.mainloop()