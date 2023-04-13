import numpy as np

#P             0  1   2  
A = np.array([[2, 3 ,4],  #v0
              [3, 2,  2], #v1
              [5, 1, 6]]) #v2
               
#H              0  1   2  
B = np.array([[22, 12, 8],   #P0
              [28, 15, 15],  #P1
              [30 ,12, 10]]) #P2
B = B.T


op = "S"
while op == "S":
    V = 3
    H = 3
    while not (V==0 or V ==1 or V == 2):
        V = int(input("Código do pesticida(0, 1, 2): "))
    while not (H==0 or H ==1 or H == 2):
        H = int(input("Código do herbívoro(0, 1, 2): "))
        
    Quant = np.sum(A[V]*B[H])
    print("O herbívoro %i ingere %i ml do pesticida %i" % (H, Quant, V) )
    
    
    

    op = input("Deseja realizar outra consulta (S/N): ").upper()
    while not (op=="S" or op == "N"):
        op = input("Deseja realizar outra consulta (S/N): ").upper()
    