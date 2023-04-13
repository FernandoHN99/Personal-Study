N = float(input("Digite quantos valores deseja utilizar: "))

I = 1
S = 0

while I <= N:
    X = float(input("Digite um valor: "))
    S = S + X**2 
    I = I + 1

print("O valor da soma dos quadrados é: %d" % S)