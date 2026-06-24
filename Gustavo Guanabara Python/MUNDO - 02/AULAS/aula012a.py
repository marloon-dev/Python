name = str(input("NAME: "))

if name == "MARLON":
    print("SEU NOME É MUITO BONITO.")
elif name == "PEDRO" or name == "MARIA" or name == "JOSÉ":
    print("SEU NOME É BEM COMUM, NO BRASIL.")
elif name == "MARTA" or name == "MARA":
    print("BELO NOME, FEMININO.")
else:
    print("SEU NOME É NORMAL.")

print("BOM DIA, {}.".format(name))