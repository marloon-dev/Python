nome = ""
continuar = True
while continuar:
    nome = nome + input("Digite um nome ") + "\n"

    x = input("Deseja continuar? Digite 'Sim' ou 'Não' ")

    if (x.upper () == "SIM"):
        continuar = True
    elif (x.upper () == "NÃO"):
        continuar = False
        print("Opção inválida. Selecione 1, 2 ou 3.")
    else:
        break
print (nome)
