# Abertura do arquivo

dados = open("UNIDADE05/ex01/dados.txt", "r")

# Leia o conteúdo do Arquivo

conteudo = dados.read()

# Imprimindo o Arquivo txt

print(conteudo)

# Fechamento o Arquivo

dados.close()