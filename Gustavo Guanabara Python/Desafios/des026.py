print("\n==== EXERCÍCIO 26 ====")

frase = input("\nFRASE: ").strip().upper()
letra = input("LETRA: ").strip().upper()

print("\nA LETRA ({}) APARECE {} VEZES.".format(letra, frase.count(letra)))
print("PRIMEIRA LETRA ({}), ESTÁ NA POSIÇÃO {}".format(letra, frase.find(letra)+1))
print("ULTIMA LETRA ({}), ESTÁ NA POSIÇÃO {}".format(letra, frase.rfind(letra)+1))

print("\n####################....100% PROGRAMA FINALIZADO....")