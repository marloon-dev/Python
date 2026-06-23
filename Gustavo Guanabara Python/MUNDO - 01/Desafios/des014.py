print("\n==== CONVERSOR DE CELSIUS EM FAHRENHEIT====\n")

# INPUT PARA DIGITAR OS GRAUS CELSIUS
graus_celsius = float(input("Temperatura em °C: "))

# CONVERSERTE CELSIUS EM FAHRENHEIT
graus_fahrenheit = (graus_celsius * 1.8) + 32

# MOSTRAR NA TELA RESULTADO
print(
    "\nGraus Celsius: {:.2f}°C".format(graus_celsius),
    "\nGraus Fahrenheit: {:.2f}°F".format(graus_fahrenheit)
)

print("\n==== Fim do programa ====\n")