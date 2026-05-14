print("\n=== Calculadora de Saúde (IMC) ===")

# ENTRADA DE DADOS
nome = input("\nNome do paciente: ")
peso = float(input("peso (kg): "))
altura = float(input("altura (m): "))

# CÁLCULO DO IMC
imc = peso / (altura ** 2)

# CLASSIFICAÇÃO DO IMC
if imc <= 18.5: 
    classificacao = "Abaixo do peso"
elif imc <18.5 or imc <= 24.9:
    classificacao = "Peso normal"
elif imc < 25 or imc <= 29.9:
    classificacao = "Sobrepeso"
elif imc < 30 or imc <= 34.9:
    classificacao = "Obesidade grau 1"
elif imc < 35 or imc <= 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

# RESULTADOS
print(f"\nPaciente: {nome}")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")    

print("\n__________________________________________________________________________________________")