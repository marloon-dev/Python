print("\n==== EXERCÍCIO 33 ====")

# 1. ENTRADA DE DADOS
print("\nDESCOBRIR O MENOR E MAIOR VALOR")
valor_1 = int(input("\nPRIMEIRO VALOR: "))
valor_2 = int(input("SEGUNDO VALOR: "))
valor_3 = int(input("TERCEIRO VALOR: "))

# 2. VERIFICAR QUEM É O MENOR
menor = valor_1
if valor_2 < valor_1 and valor_2 < valor_3:
    menor = valor_2

if valor_3 < valor_1 and valor_3 < valor_2:
    menor = valor_3

# 3. VERIFICAR QUEM É O MANIOR
maior = valor_1
if valor_2 > valor_1 and valor_2 > valor_3:
    maior = valor_2

if valor_3 > valor_1 and valor_3 > valor_2:
    maior = valor_3

# 4. EXIBIÇÃO DOS RESULTADOS
print("\nRESULTADO")
print("\nMAIOR VALOR: {:.0f}".format(maior))
print("MENOR VALOR: {:.0f}".format(menor))

print("\n####################....100% PROGRAMA FINALIZADO....")