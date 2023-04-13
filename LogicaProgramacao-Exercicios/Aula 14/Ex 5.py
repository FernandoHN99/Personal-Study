Lista = []

op = "x"

while op != "S":
    op = input("(C)adastrar, (E)ntregar, (S)air ").upper()
    
    if op == "C":
        Bebida = input("Digite a bebida: ")
        Nome = input("Nome do cliente: ")
        Lista.append([Nome, Bebida])
        
    elif op == "E":
        Entrega = Lista.pop(0)
        print("%s venha pegar o %s" % (Entrega, Entrega[1]) )
        input()
        
        