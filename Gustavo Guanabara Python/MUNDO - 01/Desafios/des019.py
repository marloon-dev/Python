print("\n====SORTEIO DE NOMES ALEATÓRIOS====")

# IMPORTAR BIBLIOTECA RANDOM
from random import choice

# ENTRADA DOS NOMES PARA O SORTEIO
nomes = []

quantidade = int(input("\nQUANTOS NOMES PARA O SORTEIO: "))

for i in range(quantidade):
    nome = input(f"NOMES {i + 1}: ")
    nomes.append(nome)

# SORTEIO 
sorteio = choice(nomes)

# IMPRIMIR NOMES A SEREM SORTEIADO NA TELA
print("\nLISTA DE NOMES:")
print("")
for nome in nomes:
    print(nome)

# IMPRIMIR NOMES SORTEADO NA TELA
print("\nNOME SORTEADO: {}".format(nome))

print("\n####################100% PROGRAMA FINALIZADO")