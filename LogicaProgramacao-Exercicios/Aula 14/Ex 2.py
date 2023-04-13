from math import sqrt


#Procedimento
def LerValores(N, X):
    I = 0 
    while I < N:
        Valor = float(input("Digite o %iº valor:  " % (I + 1) ))
        X.append(Valor)
        I = I + 1
        
    Media = sum(X)/N

    I = 0 
    Soma = 0
    while I < N:
      Soma = Soma + (X[I] - Media)**2
      I = I + 1
    
    Final = sqrt( (Soma/(N-1)) )
    
    print("A média é : %.2f" % Media)
    print("O desvio padrão é: %.2f" % Final)
    
    


#Principal
N = int(input("Deseja digitar quantos valores? "))
X = []

LerValores(N, X)

