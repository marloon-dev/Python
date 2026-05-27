# Abertudo do arquivo 
dados = open("UNIDADE05/ex01/dados.txt", "r+")

# Leia o conteúdo do arquivo
conteudo = dados.read()

# Imprimindo o conteudo
print(conteudo)

# Escrevendo no arquivo
dados.write("\n Python s2 \n")

# Fechamento o arquivo

dados.close()