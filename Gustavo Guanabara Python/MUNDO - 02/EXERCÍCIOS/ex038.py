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
    print(f"{verde}|            EXERCÍCIO - 38 🐍           |{reset}")
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

num1 = int(input("1º NÚMERO: "))
num2 = int(input("2º NÚMERO: "))
num3 = int(input("3º NÚMERO: "))

maior = num1
if num2 < num1 and num2 < num3:
    maior = num2
if num3 > num1 and num3 > num1:
    maior = num3

if num1 == num2:
    iguais = "1º E 2ª, POSIÇÃO."
elif num1 == num3:
    iguais = "1º E 3ª, POSIÇÃO."
elif num2 == num1:
    iguais = "2º E 1ª, POSIÇÃO."
elif num2 == num3:
    iguais = "2º E 3ª, POSIÇÃO."
elif num3 == num1:
    iguais = "3º E 1ª, POSIÇÃO."
elif num3 == num2:
    iguais = "3º E 2ª, POSIÇÃO."
else:
    iguais = "NENHUM NUMERO IGUAL"

print("NÚMERO MAIOR: {}".format(maior))
print("NÚMERO IGUAIS: {}".format(iguais))

fim()