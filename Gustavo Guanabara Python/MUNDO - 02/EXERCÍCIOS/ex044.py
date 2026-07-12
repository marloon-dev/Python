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
    print(f"{verde}|            EXERCÍCIO - 44 🐍           |{reset}")
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

valor = float(input("\bVALOR DO PRODUTO: € "))
print("\nFORMAS DE PAGAMENTO")
print("\n[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x cartão")
print("[ 4 ] 3x ou mais cartão")
opcao = int(input("QUAL É A OPÇÃO: "))
if opcao == 4:
    parcelas = int(input("QUANTIDADE DE PARCELAS: "))

desc1 = valor * 0.10
desc2 = valor * 0.05
acres = valor * 0.20
if opcao == 1:
    resultado = valor - desc1
elif opcao == 2:
    resultado = valor - desc2
elif opcao == 3:
    resultado = valor
elif opcao == 4:
    resultado = valor + acres

resultado = resultado * 1000

print("\nVALOR DA COMPRA: {:.2f}".format(resultado))

if opcao == 3:
    cartao = resultado / 2
    print("PARCELAS: 2x de € {:.2f}".format(cartao))

if opcao == 4:
    valor_parcelas = resultado / parcelas
    print("PARCELAS: {}x de € {:.2f}".format(parcelas, valor_parcelas))

fim()