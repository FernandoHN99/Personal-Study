N = int(input("Digite um n�mero: "))
I = 1
S = 1
N1 = N
Resposta = "sim"


while Resposta == "sim":  #para poder perguntar outras vezes (aninhadas)
    while I < N:
        S = S * (N - 1)  #fatorial
        N = N - 1
    print("O fatorial de %d �: %d" % (N1, (N1 * S)))
    Resposta = str(input("Deseja digitar um outro valor: "))  #seria o hipotetico para outros valores
    if Resposta == "sim" or Resposta == "s" or Resposta == "S":
        N = int(input("Digite um n�mero: "))
        I = 1
        S = 1
        N1 = N
    else:
        print("OK, at� a pr�xima!!")