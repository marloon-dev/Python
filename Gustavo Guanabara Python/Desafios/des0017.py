print("\n====CALCULADORA DE HIPOTENUSA====")
# IMPORTANDO O MODULO HYPOT DA BIBLIOTECA MATH
from math import hypot

# PREENCHIMENTO DOS CATETOS
print("\nDIGITE OS CATETOS")
co = float(input("\nCateto aposto: "))
ca = float(input("Cateto adjacente: "))

# CALCULO DA HIPOTENUSA
hi = hypot(co, ca)

# CALCULO DA HIPOTENUSA SEM MODULO DA BIBLIETECA MATH
# hi = (co ** 2 + ca ** 2) ** (1/2)

# IMPRIMIR RESULTADO
print("\nRESULTADO")
print("\nHipotenusa: {:.2f}".format(hi))

print("\n####################100% PROGRAMA FINALIZADO")