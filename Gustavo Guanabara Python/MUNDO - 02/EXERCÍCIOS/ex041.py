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
    print(f"{verde}|            EXERCÍCIO - 41 🐍           |{reset}")
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
from datetime import date

ano_nascimento = int(input("{}Ano nascimento: {}".format(ciano, reset)))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade < 2:
    resultado = "Precisar ter mais de 2 anos"

elif idade >= 2 and idade <=9:
    resultado = "Mirim"

elif idade >= 10 and idade <=14:
    resultado = "Infantil"

elif idade >= 15 and idade <=19:
    resultado = "Junior"

elif idade >= 20 and idade <= 25:
    resultado = "Sênior"

elif idade > 25:
    resultado = "Master"

print("{}CLASSIFICAÇÃO: {}{}".format(ciano, reset, resultado))
print("{}IDADE: {}{}".format(ciano, reset, idade))
fim()