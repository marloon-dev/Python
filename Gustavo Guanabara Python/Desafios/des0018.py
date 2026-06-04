

# IMPORTE DA BIBLIETECA MATH
from math import radians, sin, cos, tan

# DIGITE O ANGOLO EM GRAUS
angulo_graus = float(input("\nDigite o Ângulo: "))

# CONVERTER O ÂNGULO DE GRAUS PARA RADIANOS
angulo_radianos = radians(angulo_graus)

# CALCULAR SENO, COSSENO E TANGETE
se = sin(angulo_radianos)
co = cos(angulo_radianos)
ta = tan(angulo_radianos)

# IMPRIMIR NA TELA RESULTADOS
print("\nRESULTADO")
print("\nSeno: {:.4f}".format(se))
print("Consseno: {:.4f}".format(co))
print("Tangente: {:.4f}".format(ta))

print("\n####################100% PROGRAMA FINALIZADO")