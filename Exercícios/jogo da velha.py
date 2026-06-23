import tkinter as tk
from tkinter import messagebox

# Configuração da janela
janela = tk.Tk()
janela.title("Jogo da Velha")
janela.resizable(False, False)

jogador_atual = "X"
tabuleiro = [""] * 9


def verificar_vencedor():
    combinacoes = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in combinacoes:
        if (
            tabuleiro[a] != ""
            and tabuleiro[a] == tabuleiro[b] == tabuleiro[c]
        ):
            return tabuleiro[a]

    if "" not in tabuleiro:
        return "Empate"

    return None


def reiniciar():
    global jogador_atual, tabuleiro

    jogador_atual = "X"
    tabuleiro = [""] * 9

    for botao in botoes:
        botao.config(text="", state="normal")


def jogar(posicao):
    global jogador_atual

    if tabuleiro[posicao] == "":
        tabuleiro[posicao] = jogador_atual
        botoes[posicao].config(text=jogador_atual)

        resultado = verificar_vencedor()

        if resultado:
            if resultado == "Empate":
                messagebox.showinfo("Fim do jogo", "Empate!")
            else:
                messagebox.showinfo(
                    "Fim do jogo",
                    f"Jogador {resultado} venceu!"
                )

            reiniciar()
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"


# Criar botões do tabuleiro
botoes = []

for i in range(9):
    botao = tk.Button(
        janela,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: jogar(i)
    )

    botao.grid(row=i // 3, column=i % 3)

    botoes.append(botao)

janela.mainloop()