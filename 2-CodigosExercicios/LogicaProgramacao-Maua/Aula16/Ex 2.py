                                       #Função

def LerLista(Lista):
    Menor = min(Lista)
    Maior = max(Lista)
    Tupla = (Menor, Maior)
    
    return Tupla

                                      #Principal
                                      
N = int(input("Quantidade de valores: " ))
Lista = []
i = 1
for c in range(N):
    Valores = float(input("Digite o %iº valor: " % i ))
    Lista.append(Valores)
    i = i + 1
    
print("Menor valor: %.1f / Maior valor: %.1f" % LerLista(Lista) )