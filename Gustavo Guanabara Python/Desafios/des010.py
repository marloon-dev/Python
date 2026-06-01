carteira = float(input("\nValor na Carteira: R$ "))
valor_dolar = 5.06

print(
    "\nValor dolar: $ {}".format(valor_dolar),
    "\nQuantos dolar: $ {:.2f}".format(carteira / valor_dolar)
      )