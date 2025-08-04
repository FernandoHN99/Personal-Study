from math import factorial

X = int(input("Digite um valor: "))
S = 2 + X/factorial(3)
I = 0

while X**I/factorial(I) > 10**-8:
    S = S + X**I/factorial(I)
    I = I + 2

print("O valor é: %.18f " % S)