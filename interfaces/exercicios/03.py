import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 3")
janela.geometry("400x300")

contador_label = tk.Label(janela, text=f"Você clicou 0 vezes")
contador_label.pack()

contador = 0

def clicar():
    global contador
    contador += 1
    
    contador_label['text'] = f"Você clicou {contador} vezes"

def limpar():
    global contador
    contador = 0

    contador_label['text'] = f"Você clicou 0 vezes"

tk.Button(janela, text="Clicar", command=clicar).pack()
tk.Button(janela, text="Limpar", command=limpar).pack()

janela.mainloop()