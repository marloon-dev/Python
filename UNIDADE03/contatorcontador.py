contador = 0

while contador < 10:
    if contador == 1 or contador == 3:
        contador += 1
        continue

    print(contador)
    contador += 1