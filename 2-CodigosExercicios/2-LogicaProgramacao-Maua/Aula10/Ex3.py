A = int(input("M�ltiplos de: "))
B = int(input("Menores que: "))


if B == 0:
    print("N�o � poss�vel")  #Valida��o bosta ainda
    
else: 
    I = 1
    print(0)
    while I < B-1 :
        I = I + 1
        if I % A == 0:
            print(I)