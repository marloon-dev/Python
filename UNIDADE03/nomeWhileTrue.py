nome = ""
while True:
    texto = input("Digite um nome ou '0'para encerrar o programa: ")
    if texto == "0":
        print("Programa encerrado.")
        break
    else:
        nome = nome + texto +"\n"

print("\nNomes digitados:\n" + nome)    