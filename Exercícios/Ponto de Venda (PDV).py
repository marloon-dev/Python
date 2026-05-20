print()
print("\n=== Simulador de Ponto de Venda (PDV) ===")

nome = input("\nNome do cliente: ")
valor_compra = float(input("Valor da compra: R$ "))

# VALIDAÇÃO DA OPÇÃO DE PAGAMENTO
while True:
    opcao_pagamento = int(input(
        "\nSelecione a forma de pagamento "
        "\n(1 - À vista, 2 - Parcelado): "
    ))

    if opcao_pagamento < 1 or opcao_pagamento > 2:
        print("Opção inválida. Escolha 1 ou 2.")
    else:
        break

print(f"Você escolheu a forma de pagamento: {opcao_pagamento}")

# PAGAMENTO À VISTA
if opcao_pagamento == 1:

    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto

    print("\nOpção de pagamento: À vista")
    print("Desconto de 10% aplicado.")
    print(f"Valor final: R$ {valor_final:.2f}")

# PAGAMENTO PARCELADO
elif opcao_pagamento == 2:

    # VALIDAR PARCELAS
    while True:

        qtd_parcelas = int(input(
            "\nEscolha a quantidade de parcelas (1 a 12): "
        ))

        if qtd_parcelas < 1 or qtd_parcelas > 12:
            print("Quantidade inválida. Escolha entre 1 e 12.")
        else:
            break

    print(f"Você escolheu parcelar em {qtd_parcelas} vezes.")

    # 1 A 3 PARCELAS - SEM JUROS
    if qtd_parcelas <= 3:

        valor_apagar = valor_compra

        print("Pagamento parcelado sem juros.")

    # 4 A 6 PARCELAS - 10% JUROS
    elif qtd_parcelas <= 6:

        valor_apagar = valor_compra * 1.10

        print("Pagamento parcelado com juros de 10%.")

    # 7 A 12 PARCELAS - 20% JUROS
    else:

        valor_apagar = valor_compra * 1.20

        print("Pagamento parcelado com juros de 20%.")

    # VALOR DAS PARCELAS
    valor_parcela = valor_apagar / qtd_parcelas

    print(f"\nValor total a pagar: R$ {valor_apagar:.2f}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")

print("\n__________________________________________________________________________________________")