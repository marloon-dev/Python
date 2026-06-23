print("\n==== SORTEIO DE NOMES PARA APRESENTAÇÃO ====")

from random import shuffle

nomes = []

quantidade = int(input("\nQUANTOS NOMES PARA O SORTEIO: "))

for i in range(quantidade):
    nome = input(f"NOME {i + 1}: ")
    nomes.append(nome)

shuffle(nomes)

print("\nLISTA DE NOMES SORTEADA:")
print("")
for posicao, nome in enumerate(nomes, start=1):
    print(f"{posicao}º - {nome}")

print("\n#################### 100% PROGRAMA FINALIZADO")