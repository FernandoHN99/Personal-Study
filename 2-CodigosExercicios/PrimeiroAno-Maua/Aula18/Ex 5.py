D = {    "S": 0, 
         "D": 0, 
         "P": 0   }
while True:
    op = input("Tipo da operação, (D)epósito, (S)aque, (P)agamento de contas ou (F)im: ").upper()
    if op == "F":
        break
    while op == "D" or op == "P" or op == "S":
        Valor = float(input("Digite o valor: " ))
        if op in D:
            D[op] = D[op] + Valor
            op = ""        
print("Conta bancária: R$%.2f" % (D["D"] - D["S"] - D["P"]))       