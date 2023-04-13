from math import exp, sqrt

X = float(input("Dê um valor para X: "))

while not (X >= 0) :
    X = float(input("Dê um valor para X: "))



S = exp(X) + sqrt(X)
Y = 2
   
while  1/Y >= 10**-4:
    
    if Y % 2 == 0:
        S = S - 1/Y
        Y = Y + 1
        
    elif Y % 2 != 0:
        S = S + 1/Y
        Y = Y + 1        
        
print(S)