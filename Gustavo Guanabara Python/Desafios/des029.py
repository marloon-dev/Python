print("\n==== EXERCÍCIO 29 ====")

print("\nDIGITE A VELOCIDADE DA RODOVIA")

rodovia = int(input("\nVELOCIDADE DA RODOVIA: "))
carro = int(input("VELOCIDADE DO CARRO: "))

exesso = carro - rodovia

multa = exesso * 7.0

if carro <= rodovia:
    print("\nRESULTADO")
    print("\nNÃO ULTRAPASSOU A VELOCIDADE DA RODOVIA")
    print("VELOCIDADE PERMITIDA: {:.0f}km/h".format(rodovia))
    print("VELOCIDADE DO VEÍCULO: {:.0f}km/h".format(carro))
else:
    print("\nRESULTADO")
    print("\nULTRAPASSOU A VELOCIDADE DA RODOVIA")
    print("VELOCIDADE DA PERMITIDA: {:.0f}km/h".format(rodovia))
    print("VELOCIDADE DO VEÍCULO: {:.0f}km/h".format(carro))
    print("\nVALOR DA MULTA: € {:.2f}".format(multa))

print("\n####################....100% PROGRAMA FINALIZADO....")