import tkinter as tk

def dizer_ola():
    nome = campo.get()
    resultado.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Meu primeiro programa")

campo = tk.Entry(janela)
campo.pack()

botao = tk.Button(janela, text="Clique", command=dizer_ola)
botao.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()