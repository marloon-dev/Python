preco = float(input("Preço produto: € "))
desc = float(input("Porcentagem do Desc.: "))

calculo_desc = desc / 100
caculo_preco = calculo_desc * preco
print(
    "\nValor Antigo: € {:.2f}".format(preco),
    "\nPorcentagem: {:.0f}%".format(desc),
    "\nValor com Desc.: € {:.2f}".format(preco - caculo_preco)
)