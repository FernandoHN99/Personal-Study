A = float(input("Dê um valor para A: "))
X = A
while abs(X**3 - A) > 10**-6:
    X_novo = X - (X**3 - A) / (3 * X**2)
    X = X_novo

print("A Raiz cúbica de A é : %f" % X)





#A = float(input("Dê um valor para A: "))
#print("A Raiz cúbica de A é : %f" % A**(1/3))
