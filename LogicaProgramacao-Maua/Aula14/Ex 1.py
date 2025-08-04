Vezes = int(input("Deseja digitar quantos valores? "))

Lista = []
I = 0 

while I < Vezes:
    Valor = float(input("Digite o %iº valor:  " % (I + 1) ))
    Lista.append(Valor)
    I = I + 1
    
    
opcao = " "

while not (opcao == "C" or opcao == "D"): #repetição para o erro (opcional)
    
    opcao = input(("(C)rescente ou (D)ecrescente? ")).upper()

#if opcao == "C":
#    Lista.sort()
#
#else:
#    Lista.sort(reverse = True)
#
#print(Lista)
    Lista.sort( reverse = (opcao == "D" ))

print(Lista)