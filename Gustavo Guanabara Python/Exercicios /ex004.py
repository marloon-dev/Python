print("\n======== Dissecando uma Variável ========\n")

n = input("\nDigite algo: ")
print(
    "\nTipo de classe: ", type(n),
    "\nÉ número: ", n.isnumeric(),
    "\nÉ letra: ", n.isalpha(),
    "\nÉ número decimal: ", n.isdecimal(),
    "\nEstá em Maiúscula: ", n.isupper(),
    "\nÉ número e letras: ", n.isalnum(),
    "\nÉ imprimivel: ", n.isprintable(),
)    
