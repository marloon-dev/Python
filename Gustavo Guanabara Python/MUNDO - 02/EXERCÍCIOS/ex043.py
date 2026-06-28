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
    print(f"{verde}|            EXERCÍCIO - 43 🐍           |{reset}")
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

qtdpessoas = int(input("\nQuantidade de pessoas: "))

pessoas = []

for i in range(qtdpessoas):
    nome = input("\nNome: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    imc = peso / (altura ** 2)

# CLASSIFICAÇÃO DO IMC
    
    if imc <= 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 18.5 or imc <= 24.9:
        classificacao = "Peso normal"
    elif imc < 25 or imc <= 29.9:
        classificacao = "Sobrepeso"
    elif imc < 30 or imc <= 34.9:
        classificacao = "Obesidade grau 1"
    elif imc < 35 or imc <= 39.9:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

# ARMAZENAR DADOS EM UM DICIONÁRIO

    pessoa = {
        "nome": nome,
        "idade": idade,
        "altura": altura,
        "peso": peso,
        "imc": imc,
        "classificacao": classificacao
    }

# MOSTRAR RESULTADOS

    pessoas.append(pessoa)
print("\nPessoas Cadastradas:")

for pessoa in pessoas:
    print("Nome:", pessoa ["nome"])
    print("Idade:", pessoa["idade"])
    print("Altura:", pessoa["altura"])
    print("IMC:", pessoa["imc"])
    print("Classificação:", pessoa["classificacao"])

    print()


fim()