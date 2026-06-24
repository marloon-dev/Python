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
    print(f"{verde}|            EXERCÍCIO - 36 🐍           |{reset}")
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

# OPÇÕES PARA SER ESCOLHIDAS NO PROGRAMA

print(f"{ciano}=-" * 21 + reset)
print(f"{reset}|   PREENCHA COM NÚMERO PARA CONVERTER   |")
print(f"{reset}|      [1] = CONVERTER PARA BINÁRIO      |")
print(f"{reset}|      [2] = CONVERTER PARA OCTAL        |")
print(f"{reset}|      [3] = CONVERTER PARA HEXADECIMAL  |")
print(f"{ciano}=-" * 21 + reset)

# ESCOLHER UMA OPÇÃO PARA SER CONVERTIDA O NÚMERAL

while True:
    opcao = int(input("\n{}OPÇÃO: ".format(ciano)))

    if opcao in (1, 2, 3):
          break
    print("{}OPÇÃO INVÁLIDA! DIGITE 1: 2 OU 3.".format(vermelho))

# ESCOLHER UM NÚMERO
      
numero = int(input("{}NÚMERO: ".format(ciano)))

# CONDIÇÕES PARA CONVERTE O NUMERAL EM UM RESULTADO

if opcao == 1:
    resultado = bin(numero)[2:]
    converte = "BINÁRIO"

elif opcao == 2:
    resultado = oct(numero)[2:]
    converte = "OCTAL"

elif opcao == 3:
    resultado = hex(numero)[2:].upper()
    converte = "HEXADECIMAL"

# MOSTRAR NA TELA RESULTADOS

print("\n{}NÚMERAL: {}".format(verde, converte))       
print("{}RESULTADO: {}".format(verde, resultado))

print("")
fim()