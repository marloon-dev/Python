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
    print(f"{verde}|        Obrigado por praticar! 🐍        |{reset}")
    print("|                                        |")
    print(f"{verde}|          Bons estudos em Python        |{reset}")
    print(f"{ciano}=-" * 21 + reset)


inicio()

print(f"{ciano}=-" * 21 + reset)
print(f"{reset}|PREENCHA COM OS DADOS PARA VER RESULTADO|")
print(f"{ciano}=-" * 21 + reset)

# INFORMAÇÕES A SER PREENCHIDAS PELO USUÁRIO

valor_casa = float(input("{}\nVALOR DO IMÓVEL: €".format(azul)))
parcelas = int(input("{}QUANTIDADE DE ANOS: ".format(azul)))
ordenado = float(input("{}ORDENADO: €".format(azul)))

print(f"{ciano}=-" * 21 + reset)
print("{}|               RESULTADO                |".format(verde))
print(f"{ciano}=-" * 21 + reset)

# AS PARCELAS VEZES 12 PARA SABER A QUANTIDADE DE MESES

prestacao = valor_casa / (parcelas * 12)

# CONDIÇÕES PARA APROVAÇÃO DO FINANCIAMENTO

if prestacao <= ordenado * 0.30:
    resultado = "{}APROVADO".format(verde)
else:
    resultado = "{}NEGADO".format(vermelho)

# MOSTRAR NA TELA O RESULTADO

print("{}QUANTIDADE DE PARCELAS: {:.0f} MESES".format(azul, parcelas * 12))
print("{}VALOR DA PARCELA: €{:.3f}".format(azul, prestacao))
print("{}FINANCIAMENTO: {} ".format(azul, resultado))

fim() 