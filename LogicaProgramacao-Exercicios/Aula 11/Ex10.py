Nome = str(input("Escreve uma nome: ")).upper() 


P = ""                            #sair do zero
Todas_iniciais = ""               #sair do zero
validação = 1
for c in Nome:          
    if c != " ":                                        #{formar palavras
        P = P + c                   
        Último_nome = P             #ultimo nome
        
    else:
        P = ""
P = ""        
        
for c in Nome:          
    if c != " ":
        P = P + c
        
    elif c == Nome[-1]:
        P = ""  
        
    elif P == "DAS" or P == "DA" or P == "DE" or P == "DO" or P == "DOS" or P == "E":
        P = ""

    
    else:
        Primeira_Letra = P[0]
        if validação == 1:
            Todas_iniciais = Todas_iniciais + Primeira_Letra
            validação = 2
          
            P = ""
        else:
            Todas_iniciais = Todas_iniciais + "." + " " + Primeira_Letra
            P = ""

print(Último_nome + "," + " " + Todas_iniciais + ".")
        
        