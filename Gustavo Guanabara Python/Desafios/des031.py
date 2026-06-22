print("\n==== EXERCÍCIO 31 ====")

viagem = int(input("\nDIGITE QUANTIDADE DE KM: "))

if viagem <= 200:
    preco = viagem * 0.50
    resultado = "NÃO"
else:
    preco = viagem * 0.35
    resultado = "SIM"

print("\nRESULTADO")
print("\nPREÇO COM DESCONTO: {}".format(resultado))
print("QUANTIDADE DE KM: {}KM".format(viagem))
print("VALOR DA VIAGEM: € {:.2f}".format(preco))

print("\n####################....100% PROGRAMA FINALIZADO....")