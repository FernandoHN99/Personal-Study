Frase = input("Digite uma frase: ")
Letra = input("Escreva uma letra: ")

P = ""
Primeira_Letra = 0
for c in Frase:          #formar palavras
    if c != " ":
        P = P + c
        
    else:
        if P[0] == Letra:         #verificar a primeira letra
            Primeira_Letra = Primeira_Letra + 1
            P = ""
            
            
if P[0] == Letra:            #ultima letra
    Primeira_Letra = Primeira_Letra + 1


print('A letra "%s" inicia %s palavras' % (Letra, Primeira_Letra))        