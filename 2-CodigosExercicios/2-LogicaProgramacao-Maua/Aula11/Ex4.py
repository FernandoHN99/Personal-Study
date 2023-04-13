Frase = str(input("Escreve uma frase: "))
Palavra = str(input("Escreva uma palavra: "))

P = ""
Iguais = 0 

for letra in Frase:
    if letra != " ":
        P = P + letra
    else:
        
        if Palavra == P:
            Iguais = Iguais + 1
            
        P = ""  
        
if Palavra == P:
    Iguais = Iguais + 1
    
    
#print (Iguais)
if Iguais == 1:
    print("A palavra aparece na frase %s vez" % Iguais)
    
elif Iguais != 1:
    print("A palavra aparece na frase %s vezes" % Iguais)
    