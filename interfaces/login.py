import tkinter as tk
import customtkinter as ctk

ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("400x300")

tela_login = ctk.CTkFrame(janela)
tela_login.pack(fill="both", expand=True)

frame_formulario = ctk.CTkFrame(tela_login)
frame_formulario.pack()

ctk.CTkLabel(frame_formulario, text="Digite seu username").grid(row=0, column=0)
username_entry = ctk.CTkEntry(frame_formulario)
username_entry.grid(row=0, column=1)

ctk.CTkLabel(frame_formulario, text="Digite sua senha").grid(row=1, column=0)
senha_entry = ctk.CTkEntry(frame_formulario)
senha_entry.grid(row=1, column=1)

def login():
    tela_login.pack_forget()
    tela_principal.pack(fill="both", expand=True)

ctk.CTkButton(frame_formulario, text="Login", command=login).grid(row=2, columnspan=2)

tela_principal = ctk.CTkFrame(janela)
ctk.CTkLabel(tela_principal, text="Bem vindo!").pack()

janela.mainloop()