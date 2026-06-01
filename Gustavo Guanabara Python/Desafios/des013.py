salario = float(input("Salário Atual: € "))
aumento = float(input("Aumento em porcentagem: "))

aumento_porc = salario + (salario * aumento / 100)


print(
    "\nSalário Atual: € {:.2f}".format(salario),
    "\nPocentagem do aumento: {:.0f}%".format(aumento),
    "\nValor do aumento: € {:.0f}".format(salario * aumento / 100),
    "\nNovo salário: € {:.2f}".format(aumento_porc)
)