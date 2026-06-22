print("\n==== CALCULAR NOTA ====")

# DIGITA NOTAS
print("\nDIGITA O NOME E SUAS NOTA A1 E A2")
nome = str(input("\nNOME DO ALUNO: "))
a2 = float(input("\nNOTA A2: "))
a1 = float(input("NOTA A1: "))
presente = int(input("PRESENÇA: "))

# CALCULAR MÉDIA
media = (a1 + a2) / 2

# IMPRIMIDO SE OS OBJETIVO DAS CONDIÇÕES FO ALCANÇADOS
if presente < 75:
    print("\nRESULTADO DO SEMESTRE")
    print("\bNOME: {}".format(nome))
    print("PRESENÇA: {:.1f}".format(presente))
    print("MÉDIA FINAL: {:.1f}".format(media))
    print("ALUNO REPROVADO POR FALTA")

elif media >= 6:
    print("\nNOME ALUNO: {}".format(nome))
    print("PRESENÇA: {:.1f}%".format(presente))
    print("MÉDIA FINAL: {:.1f}".format(media))
    print("ALUNO APROVADO")
else:
    print("\nNOME: {}".format(nome))
    print("PRESENÇA: {:.1f}%".format(presente))
    print("MÉDIA FINAL: {:.1f}".format(media))
    print("ALUNO REPROVADO")


print("\n####################....100% PROGRAMA FINALIZADO....")