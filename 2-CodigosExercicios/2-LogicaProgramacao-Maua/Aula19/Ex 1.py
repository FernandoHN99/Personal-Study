N = int(input("Digite um número: " ))
D = { "sala": [1,2,3], "quarto": [2,2,6], "cozinha": [6,3,1] } #exemplo
L=[]
def Ordena(Dic, N):
    for chave in Dic:
        if N in Dic[chave]:
            L.append(chave)
            L.sort()
    return L

Ordena(D, N)
print(L)