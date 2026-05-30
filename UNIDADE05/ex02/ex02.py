file = open("UNIDADE05/ex02/abc.txt", "w+")
file.write("Linha 01\n")
file.write("Linha 02\n")
file.write("Linha 03\n")

file.seek(0, 0)
print("\nLendo Linhas:\n")
print(file.read()+"\n")

print("\n####################################\n")

file.seek(0,0)
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")

print("\n####################################\n")

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end="")
file.close()