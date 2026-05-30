# CRIAR E MODIFICAR ARQUIVOS:
valores_celulares = [850, 2230, 1500, 3500, 5000]
"""
"r"  --> Usado somente para ler algo.
"w"  --> Usado somenta para escrever algo.
"r+" --> Usado para ler e escrever algo.
"a"  --> Usado para acrescentar algo.
"""
#with open("UNIDADE05/ex02/valores_celulares.txt", "w") as arquivo:
#        for valor in valores_celulares:
#            arquivo.write(str(valor) + "\n")

#with open("UNIDADE05/ex02/valores_celulares.txt", "a") as arquivo:
#        for valor in valores_celulares:
#            arquivo.write(str(valor) + "\n")

#with open("UNIDADE05/ex02/valores_celulares.txt", "r") as arquivo:
#        for valor in arquivo:
#            print(valor)

with open("UNIDADE05/ex02/valores_celulares.txt", "r+") as arquivo:
        for valor in arquivo:
            print(valor)
        arquivo.write("9000"+ "\n")
        