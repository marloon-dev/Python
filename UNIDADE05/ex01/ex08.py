def criar_arquivo(nome_arquivo, conteudo):
    try:
        with open(nome_arquivo, "w") as arquivo:
        arquivo.write(conteudo)
    print(f"O arquivo "{nome_arquivo}" foi criado com sucesso!")
    except Exception as e:
    print(f"Erro ao criar o arquivo: {e}")

nome_arquivo = "MeuArquivo.txt"
conteudo = "Python s2."

criar_arquivo_txt(nome_arquivo, conteudo)
