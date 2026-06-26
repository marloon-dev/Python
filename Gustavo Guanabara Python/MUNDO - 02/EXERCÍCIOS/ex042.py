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
    print(f"{verde}|            EXERCÍCIO - 42 🐍           |{reset}")
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

r_1 = int(input("{}1° Seguimento: {}".format(ciano, reset)))
r_2 = int(input("{}2° Seguimento: {}".format(ciano, reset)))
r_3 = int(input("{}3° Seguimento: {}".format(ciano, reset)))

if r_1 < r_2 + r_3 and r_2 < r_1 + r_3 and r_3 < r_1 + r_2:
    converte = "{}Sim".format(verde)
else:
    converte = "{}Não".format(vermelho)

# SDAKDSA

if converte == "{}Não".format(vermelho):
    resultado = "{}Tipo inválido".format(vermelho)

elif r_1 == r_2 and r_1 == r_3:
    resultado = "Equilátero"

elif r_1 == r_2 or r_1 == r_3 or r_2 == r_3:
    resultado = "Isóceles"

elif r_1 != r_2 or r_1 != r_3 or r_2 != r_3:
    resultado = "Escaleno"

print("\n{}Pode ser formar um triângulo: {}{}".format(ciano, reset, converte))
print("{}Tipo de triângulo: {}{}".format(ciano, reset, resultado))

fim()