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
    print(f"{verde}|            EXERCÍCIO - 40 🐍           |{reset}")
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

a1 = float(input("{}Nota A1: {}".format(ciano, reset)))
a2 = float(input("{}Nota A2: {}".format(ciano, reset)))
presenca = int(input("{}Percentual de presença: {}".format(ciano, reset, )))

MEDIA_APROVACAO = 6.0
MEDIA_RECUPERACAO = 4.0
PRESENCA_MINIMA = 75

media = (a1 + a2) / 2

if presenca < PRESENCA_MINIMA:
    resultado = "{}Reprovado por falta".format(vermelho)
elif media >= MEDIA_APROVACAO:
    resultado = "{}Aprovado".format(verde)
elif media >= MEDIA_RECUPERACAO:
    resultado = "{}Recuperação".format(vermelho)
else:
    resultado = "{}Reprovado".format(vermelho)

print("\n{}Média: {}{:.1f}".format(ciano, reset, media))
print("{}Presença: {}{}%".format(ciano, reset, presenca))
print("{}Situação: {}".format(ciano, resultado))

fim()