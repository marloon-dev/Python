# Cores ANSI
ciano = "\033[36m"
azul = "\033[34m"
verde = "\033[32m"
vermelho = "\033[31m"
reset = "\033[m"


def inicio():
    print(f"{ciano}=-" * 21 + reset)
    print(f"{azul}|          INICIANDO O PROGRAMA          |{reset}")
    print("|                                        |")
    print(f"{verde}|            EXERCÍCIO - 36🚀            |{reset}")
    print("|                                        |")
    print(f"{verde}|          Bons estudos em Python        |{reset}")
    print(f"{ciano}=-" * 21 + reset)


def fim():
    print(f"{ciano}=-" * 21 + reset)
    print(f"{azul}|            PROGRAMA ENCERRADO          |{reset}")
    print("|                                        |")
    print(f"{verde}|        Obrigado por praticar! 🚀       |{reset}")
    print("|                                        |")
    print(f"{verde}|          Bons estudos em Python        |{reset}")
    print(f"{ciano}=-" * 21 + reset)


inicio()

print(f"{ciano}=-" * 21 + reset)
print(f"{reset}|   PREENCHA COM NUMERO PARA CONVERTER   |")
print(f"{reset}|      [1] = CONVERTER PARA BINÁRIO      |")
print(f"{reset}|      [2] = CONVERTER PARA OCTAL        |")
print(f"{reset}|      [3] = CONVERTER PARA HEXADECIMAL  |")

print(f"{ciano}=-" * 21 + reset)

while True:
    opcao = int(input("\n{}OPÇÃO: ".format(ciano)))

    if opcao in (1, 2, 3):
          break
    print("{}OPÇÃO INVÁLIDA! DIGITE 1: 2 OU 3.".format(vermelho))
      
numero = int(input("{}NÚMERO: ".format(ciano)))

if opcao == 1:
        resultado = bin(numero)[2:]

elif opcao == 2:
    resultado = oct(numero)[2:]

elif opcao == 3:
        resultado = hex(numero)[2:].upper()
       

print("{}RESULTADO: {}".format(verde, resultado))

print("")
fim()