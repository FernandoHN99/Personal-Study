# validação de dados
A = 1
B = 2
N = 1

while not (A > 0 and B >= A and N > 0):
    A = int(input("Múltiplos de: "))
    B = int(input("Menores que: "))
    C = int(input("Quantos múltiplos: "))


#principal
I = 1
I_mais = 1

print(0)
while I < B-1 and I_mais <= 2:
    I = I + 1
    if I % A == 0:
        print(I)
        I_mais+=1
           
           