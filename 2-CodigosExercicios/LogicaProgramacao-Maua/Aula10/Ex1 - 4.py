N = int(input("Digite um n�mero: "))
I = 1
S = 1
N1 = N

while I < N:
    S = S * (N - 1)
    N = N - 1
print("O fatorial de %d �: %d" % (N1, (N1 * S)))


Resposta = str(input("Deseja digitar um valor?"))

if Resposta == sim:
    N = int(input("Digite um n�mero: "))
    I = 1
    S = 1
    N1 = N
    while I < N:
        S = S * (N - 1)
        N = N - 1
        print("O fatorial de %d �: %d" % (N1, (N1 * S)))


    