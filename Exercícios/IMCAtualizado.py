print()
print("\n=== Calculadora de Saúde (IMC) ===")

# ENTRADA DE DADOS

qtdpessoas = int(input("\nQuantidade de pessoas: "))

pessoas = []

for i in range(qtdpessoas):
    nome = input("\nNome: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))
    peso = float(input("Peso (em kg): "))
    
    imc = peso / (altura ** 2)

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

    pessoa = {
        "nome": nome,
        "idade": idade,
        "altura": altura,
        "peso": peso,
        "imc": imc,
        "classificacao": classificacao
    }

    pessoas.append(pessoa)
print("\nPessoas cadastradas:\n")
for pessoa in pessoas:
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("IMC:", pessoa["imc"])
    print("Classificação:", pessoa["classificacao"])
    print() 

print("\n__________________________________________________________________________________________")