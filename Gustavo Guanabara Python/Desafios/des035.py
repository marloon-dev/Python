print("\n==== EXERCÍCIO 35 ====")


reta_1 = float(input("RETA 01: "))
reta_2 = float(input("RETA 02: "))
reta_3 = float(input("RETA 03: "))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print("RETAS PODE VIRA TRIÂNGULO: SIM")
else:
    print("RETAS PODE VIRA TRIÂNGULO: NÃO")
print("\n####################....100% PROGRAMA FINALIZADO....")