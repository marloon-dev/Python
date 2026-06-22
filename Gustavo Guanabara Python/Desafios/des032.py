from datetime import date
print("\n==== EXERCÍCIO 32 ====")

print("\nDIGITE O ANO PARA SABER SE É BISEXTO")
print("DIGITE (0), PARA PREENCHER COM ANO ATUAL")

ano = int(input("\nANO: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\nRESULTADO")
    print("\nANO: {}".format(ano))
    print("BISEXTO: SIM")
else:
    print("\nRESULTADO")
    print("\nANO: {}".format(ano))
    print("BISEXTO: NÃO")


print("\n####################....100% PROGRAMA FINALIZADO....")