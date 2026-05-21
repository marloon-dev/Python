listanomes = []

while True:
    nome = input("Digite seu nome: ")
    listanomes.append(nome)

    while True:
        continuar = int(input("Deseja continuar? 1 - Sim | 2 - Não: "))

        if continuar == 1:
            break

        elif continuar == 2:
            print("\nLista de nomes:")
            print(listanomes)
            exit()

        else:
            print("Opção inválida. Digite apenas 1 ou 2.")