print("\n====ALUGUEL DE CARROS====\n")

# QUANTIDADE DE DIAS E KM PARA SOMA
qtd_dias = int(input("Quantidade de dias: "))
qtd_kms = int(input("Quantidade de Km: "))

# CALCULO DIAS - € 60.00 POR DIA
print(
    "\nDias alguel: {}".format(qtd_dias),
    "\nValor dias: € {:.2f}".format(qtd_dias * 60.00),
    "\nKms percorridos: {:.2f} km".format(qtd_kms),
    "\nValor Kms: € {:.2f}".format(qtd_kms * 0.15),
    "\nValor Total: € {:.2f}".format((qtd_dias * 60.00)+(qtd_kms * 0.15))
)

print("\n==== Fim do programa ====\n")