print("\n=== Simulador de Análise de Crédito Estudantil (ACE) ===")

# ENTRADA DE DADOS
nome = input("\nNome do estudante: ")
renda_mensal = float(input("Renda mensal do estudante (R$): "))
despesas_mensais = float(input("Despesas mensais do estudante (R$): "))

# VALIDAÇÃO DO CURSO
while True:
    escolha_curso = input(
        "\nEscolha do curso "
        "(1 - Engenharia de Software, 2 - Medicina, 3 - Direito): "
    )

    if escolha_curso not in ["1", "2", "3"]:
        print("Opção inválida. Selecione 1, 2 ou 3.")
    else:
        break

# DEFINIÇÃO DO CURSO E VALOR
if escolha_curso == "1":
    curso = "Engenharia de Software"
    valor_curso = 850.00

elif escolha_curso == "2":
    curso = "Medicina"
    valor_curso = 1500.00

elif escolha_curso == "3":
    curso = "Direito"
    valor_curso = 1200.00

# CÁLCULO DA CAPACIDADE DE PAGAMENTO
capacidade_pagamento = max(0, renda_mensal - despesas_mensais)
capacidade_pagamento_mensal = capacidade_pagamento * 0.6

# RESULTADOS
print(f"Capacidade de pagamento mensal: R$ {capacidade_pagamento_mensal:.2f}")
print(f"\nVocê escolheu o curso: {curso}")
print(f"Valor do curso: R$ {valor_curso:.2f}")

# ANÁLISE DE CRÉDITO
if capacidade_pagamento_mensal >= valor_curso:
    print("\nCrédito aprovado! Você pode financiar o curso.")
else:
    print("\nCrédito negado. Sua capacidade de pagamento é insuficiente.")
    
print("\n__________________________________________________________________________________________")
