salario = float(input("Salário Atual: € "))
aumento = float(input("Aumento em porcentagem: "))

aumento_porc = aumento / 100
salario_novo = salario * aumento_porc

print(
    "\nSalário Atual: € {:.2f}".format(salario),
    "\nPocentagem do aumento: {:.0f}%".format(aumento),
    "\nValor do aumento: € {:.0f}".format(salario_novo),
    "\nNovo salário: € {:.2f}".format(salario_novo + salario)
)