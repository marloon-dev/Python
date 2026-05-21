# FUNÇÃO REMOVE PODE ESPECIFICAR O ITÊM A SER REMOVIDO

minhalista3 = ["João", "Maria", "Anna", "Silva"]

print("Lista original:")
print(minhalista3)

remover = input("\nDigite o nome para remover: ")

while remover in minhalista3:
    minhalista3.remove(remover)

print("\nLista Atualizada:")
print(minhalista3)