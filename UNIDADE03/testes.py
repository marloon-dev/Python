pessoas = []

quantidade = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(quantidade):
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    pessoas.append({
        "nome": nome,
        "idade": idade
    })

print("\nPessoas cadastradas:\n")

for pessoa in pessoas:
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print()