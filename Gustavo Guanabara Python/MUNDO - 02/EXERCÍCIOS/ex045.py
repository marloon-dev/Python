# CORES ANSI PARA PADRÃO DO DOCUMENTO

ciano = "\033[36m"
azul = "\033[34m"
verde = "\033[32m"
vermelho = "\033[31m"
reset = "\033[m"

# PREDEFINIÇÕES PARA O CABEÇALHO

def inicio():
    print(f"{ciano}=-" * 21 + reset)
    print(f"{azul}|          INICIANDO O PROGRAMA          |{reset}")
    print("|                                        |")
    print(f"{verde}|            EXERCÍCIO - 45 🐍           |{reset}")
    print("|                                        |")
    print(f"{verde}|          Bons estudos em Python        |{reset}")
    print(f"{ciano}=-" * 21 + reset)

# PREDEFINIÇÕES PARA O RODA PÉ

def fim():
    print(f"{ciano}=-" * 21 + reset)
    print(f"{azul}|            PROGRAMA ENCERRADO          |{reset}")
    print("|                                        |")
    print(f"{verde}|        Obrigado por praticar! 🐍       |{reset}")
    print("|                                        |")
    print(f"{verde}|          Bons estudos em Python        |{reset}")
    print(f"{ciano}=-" * 21 + reset)


inicio()

from random import randint
from time import sleep

print("SUAS OPÇÕES DE JOGADA:")
print("\n[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")

jogador = int(input("\nQUAL JOGADA: "))

computador = randint(0, 2)

print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

# JOGADA

jogadas = ["PEDRA", "PAPEL", "TESOURA"]


# QUEM VENCEU

if jogador == computador:
    resultado = "IMPATOU"
elif jogador == 0 and computador == 1:
    resultado = "PERDEU"
elif jogador == 0 and computador == 2:
    resultado = "VENCEU"
elif jogador == 1 and computador == 0:
    resultado = "VENCEU"
elif jogador == 1 and computador == 2:
    resultado = "PERDEU"
elif jogador == 2 and computador == 0:
    resultado = "PERDEU"
elif jogador == 2 and computador == 1:
    resultado = "VENCEU"


print("\nJOGADOR ESCOLHEU: {}".format(jogadas[jogador]))
print("COMPUTADOR ESCOLHEU: {}".format(jogadas[computador]))
print("\nJOGADOR {}".format(resultado))

fim()