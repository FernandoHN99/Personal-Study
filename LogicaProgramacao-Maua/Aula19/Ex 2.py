D = {}

while True: 
    Pais = input("Digite o nome do país: ").title()
    
    if Pais == "":
        break
    
    if len(Pais) < 12:
        resto = 12 - len(Pais)
        Pais = Pais + (resto*" ")    #Para ficar bonito na hora de printar 
        
    
    Medalha = input("Digite a medalha ganha: ").title()
    
    while Medalha == "Ouro" or  Medalha =="Prata" or Medalha == "Bronze":
        if Pais not in D:
            D[Pais] = {"Ouro": 0, "Prata":0, "Bronze": 0}
            D[Pais][Medalha] = D[Pais][Medalha] + 1            
        else:
            D[Pais][Medalha] = D[Pais][Medalha] + 1
            
        break
print('\n' * 40)
print("       " + "*** QUADRO DE MEDALHAS ***")
print()
print("%s %14s %7s %9s" % ("País", "Ouro", "Prata", "Bronze") )
for time in D:
    print("%s %4s %7s %8s" % (time, D[time]["Ouro"], 
                                 D[time]["Prata"],
                                 D[time]["Bronze"]) )     
    