print("\n==== EXERCÍCIO 34 ====")

print("\nDIGITE SEU ORDENADO")
ordenado = float(input("VALOR: "))

if ordenado <= 1.250:
    aumento = ordenado + (ordenado * 15 / 100)
else:
   aumento = ordenado + (ordenado * 10 / 100)

print("\nRESULTADO")
print("\nAUMENTO: € {:.3f},00".format(aumento))

print("\n####################....100% PROGRAMA FINALIZADO....")