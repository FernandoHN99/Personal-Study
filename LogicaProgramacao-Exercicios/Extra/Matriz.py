M = int(input("Digite o número de Linhas: "))  
N = int(input("Digite o número de Colunas: "))


i = 0
Contador = 1
Total = M * N

Matrix= []
Lista = []


while i < M:
    j = 0
    if i != 0 :
        Matrix.append(Lista)
        Lista = []
        i += 1
        
    else:
        Lista = []
        i += 1
        
    while j < N :
        Valor = float(input("Digite o %i° Valor:  " %Contador ))
        Lista.append(Valor)
        j += 1
        Contador += 1 
        
Matrix.append(Lista)

print("")
print(" * * * MATRIX ORIGINAL * * * ")
for linha in Matrix:
    print("")
    for elemento in linha:
        print("\t %.1f" % elemento, end=" ")
        
			# não entendi
print("")
rez = [ [Matrix[m][n] for m in range(len(Matrix))] for n in range(len(Matrix[0]))]   
for linha in rez: 
    print(linha) 





