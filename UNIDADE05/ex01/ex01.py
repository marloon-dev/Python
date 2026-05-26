# ABERTURA DO ARQUIVO

dados = open("UNIDADE05/ex01/dados.txt", "r")

# LEIA O CONTEÚDO DO ARQUIVO

conteudo = dados.read()

#IMPRIMINDO O ARQUIVO TXT

print(conteudo)

# FECHANDO O ARQUIVO

dados.close()