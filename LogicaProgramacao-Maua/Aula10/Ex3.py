A = int(input("Múltiplos de: "))
B = int(input("Menores que: "))


if B == 0:
    print("Não é possível")  #Validação bosta ainda
    
else: 
    I = 1
    print(0)
    while I < B-1 :
        I = I + 1
        if I % A == 0:
            print(I)