preco = float(input("Preço produto: € "))
desc = float(input("Porcentagem do Desc.: "))

calculo_desc = preco - (preco * desc / 100)

print(
    "\nValor Antigo: € {:.2f}".format(preco),
    "\nPorcentagem: {:.0f}%".format(desc),
    "\nValor com Desc.: € {:.2f}".format(calculo_desc)
)