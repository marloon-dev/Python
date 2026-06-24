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

# IMPORTANDO O MÓDULO DATE DA BIBLIOTECA DATETIME 

from datetime import date

# PREENCHER ANO DE NASCIMENTO

ano = int(input("{}ANO NASCIMENTO:{} ".format(ciano, reset)))

# USANDO O MÓDULO DATE, PARA PREENCHER O ANO ATUAL

ano_atual = date.today().year

# SUBTRAÇÃO PARA EXTRAIR A IDADE DO USUÁRIO

idade = ano_atual - ano

# SOMA PARA SABER QUAL O ANO PRECISAR FAZER O ALISTAMENTO

alistamento = ano + 18

# CONDIÇÕES PARA CADA SENÁRIO

if idade == 18:
    resultado = "{}SIM".format(verde)
    prazo = "{}EM DIAS".format(verde)

elif idade < 18:
    resultado = "{}NÃO".format(vermelho)
    prazo = "{}EM DIAS".format(verde)

elif idade > 18:
    resultado = "{}SIM".format(verde)
    prazo = "{}DÉBITO".format(vermelho)

# MOSTRAR RESULTADOS

print("{}PRECISA SE ALISTA: {}{}".format(ciano,reset, resultado))
print("{}IDADE: {}{:.0f}".format(ciano, reset, idade))
print("{}ANO DE ALISTAMENTO: {}{}".format(ciano, reset, alistamento))
print("{}SERVIÇO MILITAR: {}".format(ciano, prazo))

fim()