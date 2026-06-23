print("\n====PROGRAMA QUANTIDADE DE TINTA POR METROS QUADRADOS====")

largura = float(input("\nLargura em (metros): "))
altura = float(input("\nAltura em (metros): "))

resultado = largura * altura

tinta = resultado / 2

print(
    "\nTotal m²: {:.2f} m²".format(resultado),
    "\nTotal de Tinta: {:.2f} litros".format(tinta)
)