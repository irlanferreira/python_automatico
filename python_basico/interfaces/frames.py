import tkinter as tk

janela = tk.Tk()
janela.geometry("400x300")

frame1 = tk.Frame(janela)
frame1.grid(row=0, column=0)

frame2 = tk.Frame(janela)
frame2.grid(row=0, column=1)


tk.Label(frame1, text="To no frame 1").pack()
tk.Label(frame2, text="To no frame 2").pack()


janela.mainloop()