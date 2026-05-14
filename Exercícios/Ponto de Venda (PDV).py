print("=== Simulador de Ponto de Venda (PDV) ===")

nome = input("Nome do cliente: ")
valor_compra = float(input("Valor da compra: "))

# VALIDAÇÃO DA OPÇÃO DE PAGAMENTO
while True:
    opcao_pagamento = float(input(
        "Selecione a forma de pagamento"
        "(1 - À vista, 2 - Parcelado): "))
    
    if opcao_pagamento < 1 or opcao_pagamento > 2:
        print("Opção inválida. Selecione 1 ou 2.")
    else:
        break

print(f"Você escolheu a forma de pagamento: {opcao_pagamento}")


#PAGAMENTO À VISTA
if opcao_pagamento == 1:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto

    print("Opção de pagamento selecionada: À vista")
    print("Desconto de 10% aplicado.")
    print(f"Valor final a ser pago: R$ {valor_final:.2f}")

#PAGAMENTO PARCELADO
elif opcao_pagamento == 2:
    while True:     
     qtd_parcelas = int(input(
         "Escolha a quantidade de parcelas (1 a 12) vezes: "
         ))  
     
     if qtd_parcelas < 1 or qtd_parcelas > 12:
        print("Quantidade inválida. Escolha entre 1 e 12.")
     else:
         break
    print(f"Você escolheu parcelar em {qtd_parcelas} vezes.")

     # 1 ATÉ 3 PARCELAS - SEM JUROS
    if qtd_parcelas <= 3:
        valor_apagar = valor_compra

        print("Pagamento parcelado sem Juros.")

     # 4 ATÉ 6 PARCELAS - JUROS DE 10%
    elif qtd_parcelas >= 4 and qtd_parcelas <= 6:
        valor_final = valor_compra * 1.10
    
        print("Pagamento parcelado com Juros de 10%.")

    # 7 ATÉ 12 PARCELAS - JUROS DE 20%
    else:
        valor_apagar = valor_compra * 1.20
        print("Pagamento parcelado com jutos de 20%.")
    
    # CÁLCULAR O VALOR DE CADA PARCELA
    valor_pacela = valor_apagar / qtd_parcelas

    # MOSTRAR O VALOR TOTAL A PAGAR E O VALOR DE CADA PARCELA
    print(f"Valor total a ser pago: R$ {valor_apagar:.2f}")
    print(f"Valor de cada parcela: R$ {valor_pacela:.2f}")      

#OPÇÃO DE PAGAMENTO INVÁLIDA
else:
    print("Opção de pagamento inválida. Por favor, selecione 1 ou 2.")