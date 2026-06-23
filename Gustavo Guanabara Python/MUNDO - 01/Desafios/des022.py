print("\n==== EXERCÍCIO 22 ====")

# DIGITE O NOME FUNÇÃO INPUT
nome = input("\nDIGITE SEU NOME E SOBRENOME: ")

# REMOVER ESPAÇOS NO COMEÇO E NO FIM DO NOME
nome = nome.strip()

# TRANSFORMA O NOME INTEIRO EM MAIUSCULA 
nome_maiuscula = nome.upper()

# TRANSFORMA O NOME INTEIRO EM MINUSCULA
nome_minuscula = nome.lower()

# QUANTIDADE DE LETRAS O PRIMEIRO NOME
primeiro_nome = nome.split()[0]
qtd_primeiro_nome = len(primeiro_nome)

print("\nNOME COMPLETO: {}".format(nome))
print("\nNOME COMPLETO MAIUSCULO: {}".format(nome_maiuscula))
print("\nNOME COMPLETO MINUSCULO: {}".format(nome_minuscula))
print("\nQUANTIDADE DE LETRAS PRIMEIRO: {}, LETRAS AO TOTAL O NOME {}, TEM.".format(qtd_primeiro_nome, primeiro_nome))


print("\n####################....100% PROGRAMA FINALIZADO....")