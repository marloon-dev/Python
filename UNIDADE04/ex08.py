qtdpessoas = int(input("Digite a quantidade de pessoas: "))

pessoas = []

for i in range(qtdpessoas):
    listanomes = input("\nNome: ")

    pessoa = {
        "listanomes": listanomes
    }

    pessoas.append(pessoa)

print("\nLista de Nomes:")

for pessoa in pessoas:
    print("Nomes:", pessoa["listanomes"])

# REMOVER NOME
remover = input("\nDigite o nome para remover: ")

for pessoa in pessoas[:]:
    if pessoa["listanomes"] == remover:
        pessoas.remove(pessoa)

print("\nLista Atualizada:")

for pessoa in pessoas:
    print("Nomes:", pessoa["listanomes"])

print()