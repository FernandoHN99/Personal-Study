Frase = input("Digite uma frase: ").lower().split(" ")
D= {}

for palavra in Frase:
    if palavra not in D:
        D[palavra] =  1
    else:       
        D[palavra] = D[palavra] + 1
        
print(D)