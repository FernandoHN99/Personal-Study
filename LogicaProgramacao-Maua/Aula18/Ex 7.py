PAE = {"ATC003":5, "ATC006":5,"ATC009":5,"ATC030":5,
       
       "ATC001":10,"ATC004":10,"ATC007":10,"ATC010":10,
       "ATC013":10,"ATC026":10,"ATC028":10,"ATC032":10,"ATC034":10,
       
       "ATC016":40,"ATC018":40,"ATC020":40,"ATC022":40,"ATC024":40,"ATC036":40}
D = {}

N = int(input("Digite o número de PAEs inscritas: " ))
i = 1

while i <= N:
    Nome = input("Digite o código da atividade: ").upper()
    Conceito = input("Digite o conceito recebdo (C/N) ").upper()
    
    while Nome not in PAE:
        print("Atividade não cadastrada")
        Nome = input("Digite o código da atividade: ").upper()
        Conceito = input("Digite o conceito recebdo (C/N) ").upper()
        
    if Nome in PAE:
        D[Nome] = Conceito
        i = i + 1
S = 0     
Total = 0   
for codigo in D:
    Total = Total + PAE[codigo]
    if D[codigo] == "C":
        S = S + PAE[codigo]

print("Cumpriu %i de %i horas" % (S, Total) )
        