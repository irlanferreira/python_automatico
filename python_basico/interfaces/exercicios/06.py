import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Exercício 6")
janela.geometry("400x300")

tela_inicial = tk.Frame(janela, bg="lightblue")
tela_inicial.pack(fill="both", expand=True)

def nova_anotacao():
    tela_inicial.pack_forget()
    tela_anotacao.pack(fill="both", expand=True)

def salvar_anotacao():
    anotacao = anotacao_entry.get()
    if not anotacao:
        messagebox.showerror("ERRO", "Você não digitou nenhuma anotação.")
        return
    
    tk.Label(tela_inicial, text=anotacao).pack()
    messagebox.showinfo("Sucesso", "Anotação salva com sucesso!")

def voltar():
    tela_anotacao.pack_forget()
    tela_inicial.pack(fill="both", expand=True)
    

tk.Label(tela_inicial, text="Bem vindo ao seu bloco de notas!", bg="#2591a7", fg="white").pack()
tk.Button(tela_inicial, text="Nova anotação", command=nova_anotacao).pack()

tela_anotacao = tk.Frame(janela, bg="lightgreen")

anotacao_entry = tk.Entry(tela_anotacao)
anotacao_entry.pack()

tk.Button(tela_anotacao, text="Salvar", command=salvar_anotacao).pack()
tk.Button(tela_anotacao, text="Voltar", command=voltar).pack()

janela.mainloop()