nome_aluno = input("Nome: ")
a1 = float(input("Nota A1: "))
a2 = float(input("Nota A2: "))
frequencia = int(input("Frequência: "))

# Realizamos o cálculo ANTES de imprimir a Nota Final
soma = a1 + a2
               
print("Nome: ", nome_aluno)
print("Nota A1:", a1)
print("Nota A2:", a2)
print("Frequência:", frequencia)
print("Nota Final:", soma)

# Corrigido o nome da variável para 'frequencia'
if (frequencia >= 75):
    if (soma >= 6):
        print("Aprovado")
    elif (soma >= 2):
        print("Recuperação")
    else:
        print("Reprovado")
else:
    # Caso a frequência seja menor que 75%
    print("Reprovado por faltas")
