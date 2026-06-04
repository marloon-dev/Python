# IMPORTANDO O MODULO HYPOT DA BIBLIOTECA MATH
from math import hypot

# PREENCHIMENTO DOS CATETOS
co = float(input("Comprimento do cateto aposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

# CALCULO DA HIPOTENUSA
hi = hypot(co, ca)

# CALCULO DA HIPOTENUSA SEM MODULO DA BIBLIETECA MATH
# hi = (co ** 2 + ca ** 2) ** (1/2)

# IMPRIMIR RESULTADO
print("A hipotenusa: {:.2f}".format(hi))
