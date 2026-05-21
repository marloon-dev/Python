qtdpessoas = input(int("Digite a quantidade de pessoas: "))

pessoas = []

for i in range(qtdpessoas):
    nome = input("\nNome: ")

pessoa = {
    "nome": nome
}


minhalista3 = ["João", "Maria", "Anna", "Silva"]

print("Lista original:")
print(minhalista3)

remover = input("\nDigite o nome para remover: ")

while remover in minhalista3:
    minhalista3.remove(remover)

print("\nLista Atualizada:")
print(minhalista3)