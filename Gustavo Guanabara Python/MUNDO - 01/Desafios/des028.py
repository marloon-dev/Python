from random import randint
print("\n==== EXERCÍCIO 28 ====")

computador = randint(0, 1)
print(" - DIGITE UM NUMERO DE 0 À 5 - ")
numero = int(input("\nNÚMERO: "))

if computador == numero:
    print("\nRESULTADO")
    print("\nPARABÉNS ACERTOU O NUMERO")
else:
    print("\nRESULTADO")
    print("\nRESPOSTA: {:.0f}".format(computador))
    print("ERROU O NÚMERO.")

print("\n####################....100% PROGRAMA FINALIZADO....")