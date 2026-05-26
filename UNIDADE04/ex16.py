# =========================================
# CRIANDO DICIONÁRIO COM INPUT
# =========================================

dicionario = {}

print("=" * 40)
print("📦 CADASTRO DE ITENS")
print("=" * 40)

qtditens = int(input("Digite a quantidade de itens: "))

for i in range(qtditens):
    print(f"\n🔹 Item {i + 1}")

    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")

    dicionario[chave] = valor

print("\n" + "=" * 40)
print("✅ DICIONÁRIO FINAL")
print("=" * 40)

for chave, valor in dicionario.items():
    print(f"{chave} → {valor}")

print("=" * 40)