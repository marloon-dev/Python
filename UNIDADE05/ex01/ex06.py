# Abertura do arquivo

segundoArquivo = open("UNIDADE05/ex01/segundoArquivo.txt", "r")

# Leia e concatennando as linhas em uma única variável

linhas = segundoArquivo.readlines();

# Imprimindo o Arquivo txt
for linha in linhas:
    print(linha)

# Fechamento o Arquivo

segundoArquivo.close()